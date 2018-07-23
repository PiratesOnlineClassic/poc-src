from panda3d.core import Point3, VBase3
objectStruct = {
    'Objects': {
        '1161805520.84Shochet': {
            'Type': 'Region',
            'Name': 'default',
            'Objects': {
                '1161805542.95Shochet': {
                    'Type': 'Island',
                    'File': 'ParlorIsland',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Objects': {
                        '1161805566.88Shochet': {
                            'Type': 'LOD Sphere',
                            'Hpr': Point3(0.0, 0.0, 0.0),
                            'Pos': Point3(0.0, 0.0, 10.194),
                            'Radi': [159, 1159, 2159],
                            'Scale': VBase3(1.0, 1.0, 1.0)
                        }
                    },
                    'Pos': Point3(0.0, 0.0, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Visual': {
                        'Model': 'models/islands/wild_island_a_zero'
                    }
                }
            },
            'Visual': {}
        }
    },
    'Layers': {},
    'ObjectIds': {
        '1161805520.84Shochet':
        '["Objects"]["1161805520.84Shochet"]',
        '1161805542.95Shochet':
        '["Objects"]["1161805520.84Shochet"]["Objects"]["1161805542.95Shochet"]',
        '1161805566.88Shochet':
        '["Objects"]["1161805520.84Shochet"]["Objects"]["1161805542.95Shochet"]["Objects"]["1161805566.88Shochet"]'
    }
}
