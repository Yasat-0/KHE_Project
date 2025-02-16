const config = {
    type: Phaser.AUTO,
    width: 800,
    height: 600,
    backgroundColor: '#ffffff',
    physics: {
        default: 'arcade',
        arcade: {
            gravity: { y: 300 },
            debug: false
        }
    },
    scene: {
        preload: preload,
        create: create,
        update: update
    }
};

const game = new Phaser.Game(config);

let player;
let platforms;
let cursors;

function preload() {
    this.load.image('ground', 'path/to/ground.png'); // Replace with your platform image
    this.load.image('player', 'path/to/player.png'); // Replace with your player image
}

function create() {
    platforms = this.physics.add.staticGroup();

    for (let i = 0; i < 6; i++) {
        const x = Phaser.Math.Between(0, 800 - 100);
        const y = Phaser.Math.Between(0, 600 - 20);
        platforms.create(x, y, 'ground').setScale(1).refreshBody();
    }

    player = this.physics.add.sprite(400, 500, 'player');
    player.setBounce(0.2);
    player.setCollideWorldBounds(true);

    this.physics.add.collider(player, platforms);

    cursors = this.input.keyboard.createCursorKeys();
}

function update() {
    if (cursors.left.isDown) {
        player.setVelocityX(-160);
    } else if (cursors.right.isDown) {
        player.setVelocityX(160);
    } else {
        player.setVelocityX(0);
    }

    if (cursors.up.isDown && player.body.touching.down) {
        player.setVelocityY(-330);
    }
}