# Embedded file name: pirates.leveleditor.worldData.GameAreaSandbox
from panda3d.core import Point3, VBase3
objectStruct = {
    'Objects': {
        '1163553215.56sdnaik': {
            'Type': 'Region',
            'Name': 'default',
            'Objects': {
                '1163553227.34sdnaik': {
                    'Type': 'Island',
                    'File': 'GameAreaSandboxIsland',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Objects': {
                        '1164915549.7sdnaik': {
                            'Type': 'LOD Sphere',
                            'Hpr': Point3(0.0, 0.0, 0.0),
                            'Pos': Point3(0.0, 0.0, 0.449),
                            'Radi': [1855, 2855, 3855],
                            'Scale': VBase3(1.0, 1.0, 1.0)
                        }
                    },
                    'Pos': Point3(8.827, -2.15, 0.0),
                    'Visual': {
                        'Model': 'models/islands/gameAreaSandbox'
                    }
                }
            },
            'Visual': {}
        }
    },
    'Layers': {},
    'ObjectIds': {
        '1163553215.56sdnaik':
        '["Objects"]["1163553215.56sdnaik"]',
        '1163553227.34sdnaik':
        '["Objects"]["1163553215.56sdnaik"]["Objects"]["1163553227.34sdnaik"]',
        '1164915549.7sdnaik':
        '["Objects"]["1163553215.56sdnaik"]["Objects"]["1163553227.34sdnaik"]["Objects"]["1164915549.7sdnaik"]'
    }
}
