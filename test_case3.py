dag = ['localpro',
 {'aggregate0': ['1',
                 'true',
                 'simpledetector0',
                 'astutedetector0',
                 'dftdetector0',
                 'teradetector0'],
  'aggregate1': ['1',
                 'true',
                 'simpledetector1',
                 'astutedetector1',
                 'dftdetector1',
                 'teradetector1'],
  'aggregate2': ['1',
                 'true',
                 'simpledetector2',
                 'astutedetector2',
                 'dftdetector2',
                 'teradetector2'],
  'astutedetector0': ['1', 'true', 'fusioncenter0'],
  'astutedetector1': ['1', 'true', 'fusioncenter1'],
  'astutedetector2': ['1', 'true', 'fusioncenter2'],
  'dftdetector0': ['1',
                   'true',
                   'fusioncenter0',
                   'dftslave00',
                   'dftslave01',
                   'dftslave02'],
  'dftdetector1': ['1',
                   'true',
                   'fusioncenter1',
                   'dftslave10',
                   'dftslave11',
                   'dftslave12'],
  'dftdetector2': ['1',
                   'true',
                   'fusioncenter2',
                   'dftslave20',
                   'dftslave21',
                   'dftslave22'],
  'dftslave00': ['1', 'false', 'dftslave00'],
  'dftslave01': ['1', 'false', 'dftslave01'],
  'dftslave02': ['1', 'false', 'dftslave02'],
  'dftslave10': ['1', 'false', 'dftslave10'],
  'dftslave11': ['1', 'false', 'dftslave11'],
  'dftslave12': ['1', 'false', 'dftslave12'],
  'dftslave20': ['1', 'false', 'dftslave20'],
  'dftslave21': ['1', 'false', 'dftslave21'],
  'dftslave22': ['1', 'false', 'dftslave22'],
  'fusioncenter0': ['4', 'true', 'globalfusion'],
  'fusioncenter1': ['4', 'true', 'globalfusion'],
  'fusioncenter2': ['4', 'true', 'globalfusion'],
  'globalfusion': ['3', 'true', 'home'],
  'localpro': ['1', 'false', 'aggregate0', 'aggregate1', 'aggregate2'],
  'simpledetector0': ['1', 'true', 'fusioncenter0'],
  'simpledetector1': ['1', 'true', 'fusioncenter1'],
  'simpledetector2': ['1', 'true', 'fusioncenter2'],
  'teradetector0': ['1', 'true', 'fusioncenter0', 'teramaster0'],
  'teradetector1': ['1', 'true', 'fusioncenter1', 'teramaster1'],
  'teradetector2': ['1', 'true', 'fusioncenter2', 'teramaster2'],
  'teramaster0': ['1', 'false', 'teraslave00', 'teraslave01', 'teraslave02'],
  'teramaster1': ['1', 'false', 'teraslave10', 'teraslave11', 'teraslave12'],
  'teramaster2': ['1', 'false', 'teraslave20', 'teraslave21', 'teraslave22'],
  'teraslave00': ['1', 'false', 'teraslave00'],
  'teraslave01': ['1', 'false', 'teraslave01'],
  'teraslave02': ['1', 'false', 'teraslave02'],
  'teraslave10': ['1', 'false', 'teraslave10'],
  'teraslave11': ['1', 'false', 'teraslave11'],
  'teraslave12': ['1', 'false', 'teraslave12'],
  'teraslave20': ['1', 'false', 'teraslave20'],
  'teraslave21': ['1', 'false', 'teraslave21'],
  'teraslave22': ['1', 'false', 'teraslave22']},
 {'aggregate0': 'node16',
  'aggregate1': 'node20',
  'aggregate2': 'node33',
  'astutedetector0': 'node42',
  'astutedetector1': 'node7',
  'astutedetector2': 'node46',
  'dftdetector0': 'node64',
  'dftdetector1': 'node59',
  'dftdetector2': 'node28',
  'dftslave00': 'node62',
  'dftslave01': 'node26',
  'dftslave02': 'node39',
  'dftslave10': 'node18',
  'dftslave11': 'node25',
  'dftslave12': 'node42',
  'dftslave20': 'node65',
  'dftslave21': 'node40',
  'dftslave22': 'node49',
  'fusioncenter0': 'node60',
  'fusioncenter1': 'node29',
  'fusioncenter2': 'node35',
  'globalfusion': 'node54',
  'localpro': 'node4',
  'simpledetector0': 'node30',
  'simpledetector1': 'node29',
  'simpledetector2': 'node39',
  'teradetector0': 'node54',
  'teradetector1': 'node49',
  'teradetector2': 'node46',
  'teramaster0': 'node21',
  'teramaster1': 'node53',
  'teramaster2': 'node16',
  'teraslave00': 'node29',
  'teraslave01': 'node24',
  'teraslave02': 'node12',
  'teraslave10': 'node20',
  'teraslave11': 'node52',
  'teraslave12': 'node34',
  'teraslave20': 'node63',
  'teraslave21': 'node54',
  'teraslave22': 'node6'}]
schedule = ['localpro',
 {'aggregate0': ['1',
                 'true',
                 'simpledetector0',
                 'astutedetector0',
                 'dftdetector0',
                 'teradetector0'],
  'aggregate1': ['1',
                 'true',
                 'simpledetector1',
                 'astutedetector1',
                 'dftdetector1',
                 'teradetector1'],
  'aggregate2': ['1',
                 'true',
                 'simpledetector2',
                 'astutedetector2',
                 'dftdetector2',
                 'teradetector2'],
  'astutedetector0': ['1', 'true', 'fusioncenter0'],
  'astutedetector1': ['1', 'true', 'fusioncenter1'],
  'astutedetector2': ['1', 'true', 'fusioncenter2'],
  'dftdetector0': ['1',
                   'true',
                   'fusioncenter0',
                   'dftslave00',
                   'dftslave01',
                   'dftslave02'],
  'dftdetector1': ['1',
                   'true',
                   'fusioncenter1',
                   'dftslave10',
                   'dftslave11',
                   'dftslave12'],
  'dftdetector2': ['1',
                   'true',
                   'fusioncenter2',
                   'dftslave20',
                   'dftslave21',
                   'dftslave22'],
  'dftslave00': ['1', 'false', 'dftslave00'],
  'dftslave01': ['1', 'false', 'dftslave01'],
  'dftslave02': ['1', 'false', 'dftslave02'],
  'dftslave10': ['1', 'false', 'dftslave10'],
  'dftslave11': ['1', 'false', 'dftslave11'],
  'dftslave12': ['1', 'false', 'dftslave12'],
  'dftslave20': ['1', 'false', 'dftslave20'],
  'dftslave21': ['1', 'false', 'dftslave21'],
  'dftslave22': ['1', 'false', 'dftslave22'],
  'fusioncenter0': ['4', 'true', 'globalfusion'],
  'fusioncenter1': ['4', 'true', 'globalfusion'],
  'fusioncenter2': ['4', 'true', 'globalfusion'],
  'globalfusion': ['3', 'true', 'home'],
  'localpro': ['1', 'false', 'aggregate0', 'aggregate1', 'aggregate2'],
  'simpledetector0': ['1', 'true', 'fusioncenter0'],
  'simpledetector1': ['1', 'true', 'fusioncenter1'],
  'simpledetector2': ['1', 'true', 'fusioncenter2'],
  'teradetector0': ['1', 'true', 'fusioncenter0', 'teramaster0'],
  'teradetector1': ['1', 'true', 'fusioncenter1', 'teramaster1'],
  'teradetector2': ['1', 'true', 'fusioncenter2', 'teramaster2'],
  'teramaster0': ['1', 'false', 'teraslave00', 'teraslave01', 'teraslave02'],
  'teramaster1': ['1', 'false', 'teraslave10', 'teraslave11', 'teraslave12'],
  'teramaster2': ['1', 'false', 'teraslave20', 'teraslave21', 'teraslave22'],
  'teraslave00': ['1', 'false', 'teraslave00'],
  'teraslave01': ['1', 'false', 'teraslave01'],
  'teraslave02': ['1', 'false', 'teraslave02'],
  'teraslave10': ['1', 'false', 'teraslave10'],
  'teraslave11': ['1', 'false', 'teraslave11'],
  'teraslave12': ['1', 'false', 'teraslave12'],
  'teraslave20': ['1', 'false', 'teraslave20'],
  'teraslave21': ['1', 'false', 'teraslave21'],
  'teraslave22': ['1', 'false', 'teraslave22']},
 {'aggregate0': ['aggregate0',
                 'ubuntu-s-1vcpu-3gb-blr1-08',
                 'root',
                 'anrgapac'],
  'aggregate1': ['aggregate1',
                 'ubuntu-s-1vcpu-3gb-nyc1-01',
                 'root',
                 'anrgapac'],
  'aggregate2': ['aggregate2',
                 'ubuntu-s-1vcpu-3gb-ams3-05',
                 'root',
                 'anrgapac'],
  'astutedetector0': ['astutedetector0',
                      'ubuntu-s-1vcpu-3gb-lon1-06',
                      'root',
                      'anrgapac'],
  'astutedetector1': ['astutedetector1',
                      'ubuntu-2gb-nyc2-02',
                      'root',
                      'anrgapac'],
  'astutedetector2': ['astutedetector2',
                      'ubuntu-s-1vcpu-3gb-sgp1-05',
                      'root',
                      'anrgapac'],
  'dftdetector0': ['dftdetector0',
                   'ubuntu-s-1vcpu-3gb-sfo2-03',
                   'root',
                   'anrgapac'],
  'dftdetector1': ['dftdetector1',
                   'ubuntu-s-1vcpu-3gb-blr1-03',
                   'root',
                   'anrgapac'],
  'dftdetector2': ['dftdetector2',
                   'ubuntu-s-1vcpu-3gb-nyc1-09',
                   'root',
                   'anrgapac'],
  'dftslave00': ['dftslave00',
                 'ubuntu-s-1vcpu-3gb-sfo2-01',
                 'root',
                 'anrgapac'],
  'dftslave01': ['dftslave01',
                 'ubuntu-s-1vcpu-3gb-nyc1-07',
                 'root',
                 'anrgapac'],
  'dftslave02': ['dftslave02',
                 'ubuntu-s-1vcpu-3gb-lon1-03',
                 'root',
                 'anrgapac'],
  'dftslave10': ['dftslave10',
                 'ubuntu-s-1vcpu-3gb-blr1-10',
                 'root',
                 'anrgapac'],
  'dftslave11': ['dftslave11',
                 'ubuntu-s-1vcpu-3gb-nyc1-06',
                 'root',
                 'anrgapac'],
  'dftslave12': ['dftslave12',
                 'ubuntu-s-1vcpu-3gb-lon1-06',
                 'root',
                 'anrgapac'],
  'dftslave20': ['dftslave20',
                 'ubuntu-s-1vcpu-3gb-sfo2-04',
                 'root',
                 'anrgapac'],
  'dftslave21': ['dftslave21',
                 'ubuntu-s-1vcpu-3gb-lon1-04',
                 'root',
                 'anrgapac'],
  'dftslave22': ['dftslave22',
                 'ubuntu-s-1vcpu-3gb-sgp1-08',
                 'root',
                 'anrgapac'],
  'fusioncenter0': ['fusioncenter0',
                    'ubuntu-s-1vcpu-3gb-blr1-04',
                    'root',
                    'anrgapac'],
  'fusioncenter1': ['fusioncenter1',
                    'ubuntu-s-1vcpu-3gb-ams3-01',
                    'root',
                    'anrgapac'],
  'fusioncenter2': ['fusioncenter2',
                    'ubuntu-s-1vcpu-3gb-ams3-07',
                    'root',
                    'anrgapac'],
  'globalfusion': ['globalfusion',
                   'ubuntu-s-1vcpu-3gb-nyc3-04',
                   'root',
                   'anrgapac'],
  'home': ['home', 'ubuntu-2gb-ams2-04', 'root', 'anrgapac'],
  'localpro': ['localpro', 'ubuntu-2gb-ams2-03', 'root', 'anrgapac'],
  'simpledetector0': ['simpledetector0',
                      'ubuntu-s-1vcpu-3gb-ams3-02',
                      'root',
                      'anrgapac'],
  'simpledetector1': ['simpledetector1',
                      'ubuntu-s-1vcpu-3gb-ams3-01',
                      'root',
                      'anrgapac'],
  'simpledetector2': ['simpledetector2',
                      'ubuntu-s-1vcpu-3gb-lon1-03',
                      'root',
                      'anrgapac'],
  'teradetector0': ['teradetector0',
                    'ubuntu-s-1vcpu-3gb-nyc3-04',
                    'root',
                    'anrgapac'],
  'teradetector1': ['teradetector1',
                    'ubuntu-s-1vcpu-3gb-sgp1-08',
                    'root',
                    'anrgapac'],
  'teradetector2': ['teradetector2',
                    'ubuntu-s-1vcpu-3gb-sgp1-05',
                    'root',
                    'anrgapac'],
  'teramaster0': ['teramaster0',
                  'ubuntu-s-1vcpu-3gb-nyc1-02',
                  'root',
                  'anrgapac'],
  'teramaster1': ['teramaster1',
                  'ubuntu-s-1vcpu-3gb-nyc3-03',
                  'root',
                  'anrgapac'],
  'teramaster2': ['teramaster2',
                  'ubuntu-s-1vcpu-3gb-blr1-08',
                  'root',
                  'anrgapac'],
  'teraslave00': ['teraslave00',
                  'ubuntu-s-1vcpu-3gb-ams3-01',
                  'root',
                  'anrgapac'],
  'teraslave01': ['teraslave01',
                  'ubuntu-s-1vcpu-3gb-nyc1-05',
                  'root',
                  'anrgapac'],
  'teraslave02': ['teraslave02',
                  'ubuntu-s-1vcpu-3gb-sgp1-01',
                  'root',
                  'anrgapac'],
  'teraslave10': ['teraslave10',
                  'ubuntu-s-1vcpu-3gb-nyc1-01',
                  'root',
                  'anrgapac'],
  'teraslave11': ['teraslave11',
                  'ubuntu-s-1vcpu-3gb-nyc3-02',
                  'root',
                  'anrgapac'],
  'teraslave12': ['teraslave12',
                  'ubuntu-s-1vcpu-3gb-ams3-06',
                  'root',
                  'anrgapac'],
  'teraslave20': ['teraslave20',
                  'ubuntu-s-1vcpu-3gb-sfo2-02',
                  'root',
                  'anrgapac'],
  'teraslave21': ['teraslave21',
                  'ubuntu-s-1vcpu-3gb-nyc3-04',
                  'root',
                  'anrgapac'],
  'teraslave22': ['teraslave22', 'ubuntu-2gb-fra1-02', 'root', 'anrgapac']}]
