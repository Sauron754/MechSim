import os

__all__ = ['exceptions.analysisExceptions', 'exceptions.frontEndExceptions', 
			'exceptions.simCoreExceptions'] #enter All submodules

moduleVersion = 'INVALID'

modulePath = os.path.dirname(exceptions.analysisExceptions.__file__)
modulePathSegments = modulePath.split("/")
subdirectoryCount = len(array)
modulePathReal = []
for iteration in range(subdirectoryCount - 1):
	modulePathReal.append(modulePathSegments[iteration])

settingsFile = open(modulePathReal, 'w')
settingsFileContent = 'MechSim_installDirectory = ' + modulePathReal + '\n' + 'MechSim_version = ' + moduleVersion
settingsFile.write(settingsFileContent)