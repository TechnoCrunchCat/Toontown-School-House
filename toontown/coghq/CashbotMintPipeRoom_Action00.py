import random

from toontown.coghq.SpecImports import *
GlobalEntities = {1000: {'type': 'levelMgr',
        'name': 'LevelMgr',
        'comment': '',
        'parentEntId': 0,
        'cogLevel': 0,
        'farPlaneDistance': 1500,
        'modelFilename': 'phase_10/models/cashbotHQ/ZONE13a',
        'wantDoors': 1},
 1001: {'type': 'editMgr',
        'name': 'EditMgr',
        'parentEntId': 0,
        'insertEntity': None,
        'removeEntity': None,
        'requestNewEntity': None,
        'requestSave': None},
 0: {'type': 'zone',
     'name': 'UberZone',
     'comment': '',
     'parentEntId': 0,
     'scale': 1,
     'description': '',
     'visibility': []},
 10025: {'type': 'attribModifier',
         'name': 'strength',
         'comment': '',
         'parentEntId': 10002,
         'attribName': 'strength',
         'recursive': 1,
         'typeName': 'goon',
         'value': '10'},
 10001: {'type': 'goon', #red goon
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 10000,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': random.choice([0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8]),
         'attackRadius': random.choice([7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),
         'crushCellId': None,
         'goonType': 'pg',
         'gridId': None,
         'hFov': 70,
         'strength': random.choice([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]),
         'velocity': random.choice([3, 4, 5, 6, 7, 8, 9])},
 10005: {'type': 'goon', #red goon
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 10003,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': random.choice([0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8]),
         'attackRadius': random.choice([7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),
         'crushCellId': None,
         'goonType': 'pg',
         'gridId': None,
         'hFov': 70,
         'strength': random.choice([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]),
         'velocity': random.choice([3, 4, 5, 6, 7, 8, 9])},
 10006: {'type': 'goon', #red goon
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 10004,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': random.choice([0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8]),
         'attackRadius': random.choice([7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),
         'crushCellId': None,
         'goonType': 'pg',
         'gridId': None,
         'hFov': 70,
         'strength': random.choice([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]),
         'velocity': random.choice([3, 4, 5, 6, 7, 8, 9])},
 10014: {'type': 'goon', #red goon
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 10013,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': random.choice([0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8]),
         'attackRadius': random.choice([7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),
         'crushCellId': None,
         'goonType': 'pg',
         'gridId': None,
         'hFov': 70,
         'strength': random.choice([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]),
         'velocity': random.choice([3, 4, 5, 6, 7, 8, 9])},
 10016: {'type': 'goon', #red goon
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 10015,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': random.choice([0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8]),
         'attackRadius': random.choice([7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),
         'crushCellId': None,
         'goonType': 'pg',
         'gridId': None,
         'hFov': 70,
         'strength': random.choice([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]),
         'velocity': random.choice([3, 4, 5, 6, 7, 8, 9])},
 10018: {'type': 'goon', #red goon
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 10017,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': random.choice([0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8]),
         'attackRadius': random.choice([7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),
         'crushCellId': None,
         'goonType': 'pg',
         'gridId': None,
         'hFov': 70,
         'strength': random.choice([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]),
         'velocity': random.choice([3, 4, 5, 6, 7, 8, 9])},
 10021: {'type': 'goon', #red goon
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 10020,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': random.choice([0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8]),
         'attackRadius': random.choice([7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),
         'crushCellId': None,
         'goonType': 'pg',
         'gridId': None,
         'hFov': 70,
         'strength': random.choice([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]),
         'velocity': random.choice([3, 4, 5, 6, 7, 8, 9])},
 10024: {'type': 'goon', #red goon
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 10023,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': random.choice([0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8]),
         'attackRadius': random.choice([7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),
         'crushCellId': None,
         'goonType': 'pg',
         'gridId': None,
         'hFov': 70,
         'strength': random.choice([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]),
         'velocity': random.choice([3, 4, 5, 6, 7, 8, 9])},
 10035: {'type': 'healBarrel',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 10037,
         'pos': Point3(-56.3795814514, 0.0, 0.0),
         'hpr': Vec3(106.821411133, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0),
         'rewardPerGrab': random.choice([6, 7, 8, 9, 10, 11, 12, 13]),
         'rewardPerGrabMax': 0},
 10036: {'type': 'healBarrel',
         'name': 'copy of <unnamed>',
         'comment': '',
         'parentEntId': 10037,
         'pos': Point3(15.3852472305, 21.0357513428, 0.0),
         'hpr': Vec3(52.4314079285, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0),
         'rewardPerGrab': random.choice([6, 7, 8, 9, 10, 11, 12, 13]),
         'rewardPerGrabMax': 0},
 10029: {'type': 'model',
         'name': 'rightPillar',
         'comment': '',
         'parentEntId': 10032,
         'pos': Point3(0.0, -22.3441867828, 0.0),
         'hpr': Point3(0.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0),
         'collisionsOnly': 0,
         'flattenType': 'light',
         'loadType': 'loadModelCopy',
         'modelPath': 'phase_10/models/cashbotHQ/pipes_A1'},
 10030: {'type': 'model',
         'name': 'leftPillar',
         'comment': '',
         'parentEntId': 10032,
         'pos': Point3(0.0, 21.9451503754, 0.0),
         'hpr': Point3(0.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0),
         'collisionsOnly': 0,
         'flattenType': 'light',
         'loadType': 'loadModelCopy',
         'modelPath': 'phase_10/models/cashbotHQ/pipes_A1'},
 10033: {'type': 'model',
         'name': 'backPillar',
         'comment': '',
         'parentEntId': 10032,
         'pos': Point3(41.4432792664, 0.0, 0.0),
         'hpr': Point3(0.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0),
         'collisionsOnly': 0,
         'flattenType': 'light',
         'loadType': 'loadModelCopy',
         'modelPath': 'phase_10/models/cashbotHQ/pipes_A1'},
 10034: {'type': 'model',
         'name': 'frontPillar',
         'comment': '',
         'parentEntId': 10032,
         'pos': Point3(-41.0848464966, 0.0, 0.0),
         'hpr': Point3(0.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0),
         'collisionsOnly': 0,
         'flattenType': 'light',
         'loadType': 'loadModelCopy',
         'modelPath': 'phase_10/models/cashbotHQ/pipes_A1'},
 10039: {'type': 'model',
         'name': 'rightPillar',
         'comment': '',
         'parentEntId': 10038,
         'pos': Point3(0.0, -66.8615875244, 0.0),
         'hpr': Point3(0.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0),
         'collisionsOnly': 0,
         'flattenType': 'light',
         'loadType': 'loadModelCopy',
         'modelPath': 'phase_10/models/cashbotHQ/pipes_A1'},
 10040: {'type': 'model',
         'name': 'leftPillar',
         'comment': '',
         'parentEntId': 10038,
         'pos': Point3(0.0, 67.0966033936, 0.0),
         'hpr': Point3(0.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0),
         'collisionsOnly': 0,
         'flattenType': 'light',
         'loadType': 'loadModelCopy',
         'modelPath': 'phase_10/models/cashbotHQ/pipes_A1'},
 10042: {'type': 'model',
         'name': 'frontRightPillar',
         'comment': '',
         'parentEntId': 10043,
         'pos': Point3(0.0, -22.5711078644, 0.0),
         'hpr': Point3(0.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0),
         'collisionsOnly': 0,
         'flattenType': 'light',
         'loadType': 'loadModelCopy',
         'modelPath': 'phase_10/models/cashbotHQ/pipes_A1'},
 10044: {'type': 'model',
         'name': 'frontLeftPillar',
         'comment': '',
         'parentEntId': 10043,
         'pos': Point3(0.0, 22.1686630249, 0.0),
         'hpr': Point3(0.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0),
         'collisionsOnly': 0,
         'flattenType': 'light',
         'loadType': 'loadModelCopy',
         'modelPath': 'phase_10/models/cashbotHQ/pipes_A1'},
 10046: {'type': 'model',
         'name': 'frontRightPillar',
         'comment': '',
         'parentEntId': 10045,
         'pos': Point3(0.0, -22.5711078644, 0.0),
         'hpr': Point3(0.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0),
         'collisionsOnly': 0,
         'flattenType': 'light',
         'loadType': 'loadModelCopy',
         'modelPath': 'phase_10/models/cashbotHQ/pipes_A1'},
 10047: {'type': 'model',
         'name': 'frontLeftPillar',
         'comment': '',
         'parentEntId': 10045,
         'pos': Point3(0.0, 22.1686630249, 0.0),
         'hpr': Point3(0.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0),
         'collisionsOnly': 0,
         'flattenType': 'light',
         'loadType': 'loadModelCopy',
         'modelPath': 'phase_10/models/cashbotHQ/pipes_A1'},
 10049: {'type': 'model',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 10048,
         'pos': Point3(0.949898421764, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': Vec3(1.29060935974, 1.29060935974, 1.29060935974),
         'collisionsOnly': 0,
         'flattenType': 'light',
         'loadType': 'loadModelCopy',
         'modelPath': 'phase_10/models/cashbotHQ/crates_F1.bam'},
 10050: {'type': 'model',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 10048,
         'pos': Point3(-13.1818971634, -7.17138242722, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0),
         'collisionsOnly': 0,
         'flattenType': 'light',
         'loadType': 'loadModelCopy',
         'modelPath': 'phase_10/models/cashbotHQ/crates_E.bam'},
 10051: {'type': 'model',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 10048,
         'pos': Point3(0.968334257603, -13.3785037994, 0.0),
         'hpr': Vec3(180.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0),
         'collisionsOnly': 0,
         'flattenType': 'light',
         'loadType': 'loadModelCopy',
         'modelPath': 'phase_10/models/cashbotHQ/crates_C1.bam'},
 10053: {'type': 'model',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 10052,
         'pos': Point3(0.606362164021, -12.1353359222, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0),
         'collisionsOnly': 0,
         'flattenType': 'light',
         'loadType': 'loadModelCopy',
         'modelPath': 'phase_10/models/cashbotHQ/crates_G1.bam'},
 10054: {'type': 'model',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 10052,
         'pos': Point3(7.85215950012, 20.0426883698, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': Vec3(1.16659212112, 1.16659212112, 1.16659212112),
         'collisionsOnly': 0,
         'flattenType': 'light',
         'loadType': 'loadModelCopy',
         'modelPath': 'phase_10/models/cashbotHQ/crates_E.bam'},
 10055: {'type': 'model',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 10052,
         'pos': Point3(13.5166940689, -0.819138884544, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': Vec3(1.51914477348, 1.51914477348, 1.51914477348),
         'collisionsOnly': 0,
         'flattenType': 'light',
         'loadType': 'loadModelCopy',
         'modelPath': 'phase_10/models/cashbotHQ/crates_D.bam'},
 10056: {'type': 'model',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 10052,
         'pos': Point3(10.8745326996, 4.61703014374, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0),
         'collisionsOnly': 0,
         'flattenType': 'light',
         'loadType': 'loadModelCopy',
         'modelPath': 'phase_10/models/cashbotHQ/crates_C1.bam'},
 10057: {'type': 'model',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 10052,
         'pos': Point3(31.8470001221, -14.5645837784, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': Vec3(1.1728117466, 1.1728117466, 1.1728117466),
         'collisionsOnly': 0,
         'flattenType': 'light',
         'loadType': 'loadModelCopy',
         'modelPath': 'phase_10/models/cashbotHQ/crates_A.bam'},
 10058: {'type': 'model',
         'name': 'copy of <unnamed>',
         'comment': '',
         'parentEntId': 10052,
         'pos': Point3(31.9369258881, 14.3037395477, 0.0),
         'hpr': Point3(90.0, 0.0, 0.0),
         'scale': Vec3(1.1728117466, 1.1728117466, 1.1728117466),
         'collisionsOnly': 0,
         'flattenType': 'light',
         'loadType': 'loadModelCopy',
         'modelPath': 'phase_10/models/cashbotHQ/crates_A.bam'},
 10002: {'type': 'nodepath',
         'name': 'goons',
         'comment': '',
         'parentEntId': 0,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Point3(270.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0)},
 10007: {'type': 'nodepath',
         'name': 'rightElbow',
         'comment': '',
         'parentEntId': 10027,
         'pos': Point3(43.3083152771, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0)},
 10008: {'type': 'nodepath',
         'name': 'leftElbow',
         'comment': '',
         'parentEntId': 10026,
         'pos': Point3(-38.578956604, -2.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0)},
 10009: {'type': 'nodepath',
         'name': 'nearRight',
         'comment': '',
         'parentEntId': 10027,
         'pos': Point3(25.6041526794, -41.3753585815, 0.0),
         'hpr': Vec3(320.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0)},
 10010: {'type': 'nodepath',
         'name': 'nearLeft',
         'comment': '',
         'parentEntId': 10026,
         'pos': Point3(-25.6000003815, -41.3800010681, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': 1},
 10011: {'type': 'nodepath',
         'name': 'farRight',
         'comment': '',
         'parentEntId': 10027,
         'pos': Point3(25.6000003815, 41.3800010681, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': 1},
 10012: {'type': 'nodepath',
         'name': 'farLeft',
         'comment': '',
         'parentEntId': 10026,
         'pos': Point3(-25.6000003815, 41.3800010681, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': 1},
 10019: {'type': 'nodepath',
         'name': 'entrance',
         'comment': '',
         'parentEntId': 10002,
         'pos': Point3(0.0, -82.5020980835, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0)},
 10022: {'type': 'nodepath',
         'name': 'exit',
         'comment': '',
         'parentEntId': 10002,
         'pos': Point3(0.0, 88.4478759766, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0)},
 10026: {'type': 'nodepath',
         'name': 'left',
         'comment': '',
         'parentEntId': 10002,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': 1},
 10027: {'type': 'nodepath',
         'name': 'right',
         'comment': '',
         'parentEntId': 10002,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': 1},
 10028: {'type': 'nodepath',
         'name': 'props',
         'comment': '',
         'parentEntId': 0,
         'pos': Point3(0.0, -1.80477809906, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0)},
 10031: {'type': 'nodepath',
         'name': 'pillars',
         'comment': '',
         'parentEntId': 10028,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': 1},
 10032: {'type': 'nodepath',
         'name': 'centerPillars',
         'comment': '',
         'parentEntId': 10031,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': 1},
 10037: {'type': 'nodepath',
         'name': 'barrels',
         'comment': '',
         'parentEntId': 0,
         'pos': Point3(102.779998779, -1.24000000954, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': 1},
 10038: {'type': 'nodepath',
         'name': 'outerPillars',
         'comment': '',
         'parentEntId': 10031,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': 1},
 10043: {'type': 'nodepath',
         'name': 'frontPillars',
         'comment': '',
         'parentEntId': 10031,
         'pos': Point3(-89.9665527344, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0)},
 10045: {'type': 'nodepath',
         'name': 'backPillars',
         'comment': '',
         'parentEntId': 10031,
         'pos': Point3(89.9700012207, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0)},
 10048: {'type': 'nodepath',
         'name': 'frontProps',
         'comment': '',
         'parentEntId': 10028,
         'pos': Point3(-100.412567139, -10.8835134506, 0.0),
         'hpr': Vec3(270.0, 0.0, 0.0),
         'scale': Vec3(1.66847121716, 1.66847121716, 1.66847121716)},
 10052: {'type': 'nodepath',
         'name': 'backProps',
         'comment': '',
         'parentEntId': 10028,
         'pos': Point3(100.0, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': 1},
 10000: {'type': 'path',
         'name': 'triangle',
         'comment': '',
         'parentEntId': 10008,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': 1,
         'pathIndex': 1,
         'pathScale': 1.5},
 10003: {'type': 'path',
         'name': 'square',
         'comment': '',
         'parentEntId': 10007,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': 1,
         'pathIndex': 0,
         'pathScale': 1.0},
 10004: {'type': 'path',
         'name': 'bowtie',
         'comment': '',
         'parentEntId': 10009,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': 1,
         'pathIndex': 2,
         'pathScale': 1.0},
 10013: {'type': 'path',
         'name': 'square',
         'comment': '',
         'parentEntId': 10010,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': 1,
         'pathIndex': 0,
         'pathScale': 1.0},
 10015: {'type': 'path',
         'name': 'square',
         'comment': '',
         'parentEntId': 10011,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': 1,
         'pathIndex': 0,
         'pathScale': 1.0},
 10017: {'type': 'path',
         'name': 'square',
         'comment': '',
         'parentEntId': 10012,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': 1,
         'pathIndex': 0,
         'pathScale': 1.0},
 10020: {'type': 'path',
         'name': 'pace',
         'comment': '',
         'parentEntId': 10019,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': 1,
         'pathIndex': 3,
         'pathScale': 1.0},
 10023: {'type': 'path',
         'name': 'pace',
         'comment': '',
         'parentEntId': 10022,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': 1,
         'pathIndex': 3,
         'pathScale': 1.0}}
Scenario0 = {}
levelSpec = {'globalEntities': GlobalEntities,
 'scenarios': [Scenario0]}
