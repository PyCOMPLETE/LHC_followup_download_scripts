import time

t_fill_start = 1527662512.98
t_fill_end = 1527704298.4750001

varlist = ['QBBI_A31L2_TT824.POSST',
 'QQBI_13L5_TT824.POSST',
 'QBBI_B13R4_TT826.POSST',
 'QBBI_A34L5_TT826.POSST']


print('Start import')
import pytimber
print('Get instance')
props={"spark.executor.memory":"8G",
       "spark.executor.cores":"20",
#        "spark.yarn.appMasterEnv.JAVA_HOME":"/var/nxcals/jdk1.8.0_121",
#        "spark.executorEnv.JAVA_HOME":"/var/nxcals/jdk1.8.0_121",
#        "spark.yarn.jars":"hdfs:////project/nxcals/lib/spark-2.4.0/*.jar",
#        "spark.yarn.am.extraLibraryPath":"/usr/lib/hadoop/lib/native",
#        "spark.executor.extraLibraryPath":"/usr/lib/hadoop/lib/native",
#        "spark.yarn.historyServer.address":"ithdp1001.cern.ch:18080",
#        "spark.yarn.access.hadoopFileSystems":"nxcals",
#        "spark.sql.caseSensitive":"true"
}
from pytimber.sparkresources import SparkResources
db = pytimber.LoggingDB(source='nxcals',
        sparkconf=SparkResources.CUSTOM.name,
        sparkprops=props
        )
print('Start download')
t1 = time.time()
res = db.get(varlist, t_fill_start, t_fill_end)
t2 = time.time()

print(f'Elapsed {t2-t1}s')
