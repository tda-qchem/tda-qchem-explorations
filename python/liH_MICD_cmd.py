#!/usr/bin/env python

from paraview.simple import *

# create a new 'XML Image Data Reader'
start_data_omega_bzvti = XMLImageDataReader(FileName=['data/LiH_MICD/vti/start_data_omega_bz.vti'])

# create a new 'Calculator'
calculator1 = Calculator(Input=start_data_omega_bzvti)
calculator1.ResultArrayName = 'oppositeOmega'
calculator1.Function = '-omega_bz'

# create a new 'TTK PersistentGenerators'
tTKPersistentGenerators1 = TTKPersistentGenerators(Input=calculator1)
tTKPersistentGenerators1.ScalarField = ['POINTS', 'oppositeOmega']

# create a new 'Threshold'
threshold1 = Threshold(Input=tTKPersistentGenerators1)
threshold1.Scalars = ['CELLS', 'Persistence']
threshold1.LowerThreshold = 0.5
threshold1.UpperThreshold = 0.8493308367608376

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother2 = TTKGeometrySmoother(Input=threshold1)
tTKGeometrySmoother2.IterationNumber = 2

# create a new 'TTK TopologicalSimplificationByPersistence'
tTKTopologicalSimplificationByPersistence1 = TTKTopologicalSimplificationByPersistence(Input=start_data_omega_bzvti)
tTKTopologicalSimplificationByPersistence1.InputArray = ['POINTS', 'omega_bz']
tTKTopologicalSimplificationByPersistence1.PersistenceThreshold = 0.5

# create a new 'TTK MorseSmaleComplex'
tTKMorseSmaleComplex1 = TTKMorseSmaleComplex(Input=tTKTopologicalSimplificationByPersistence1)
tTKMorseSmaleComplex1.ScalarField = ['POINTS', 'omega_bz']
tTKMorseSmaleComplex1.AscendingSegmentation = 0
tTKMorseSmaleComplex1.DescendingSegmentation = 0
tTKMorseSmaleComplex1.MorseSmaleComplexSegmentation = 0
tTKMorseSmaleComplex1.ReturnSaddleConnectors = 1
tTKMorseSmaleComplex1.SaddleConnectorsPersistenceThreshold = 0.5

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother1 = TTKGeometrySmoother(Input=OutputPort(tTKMorseSmaleComplex1,1))
tTKGeometrySmoother1.IterationNumber = 1000

# create a new 'Threshold'
threshold2 = Threshold(Input=tTKGeometrySmoother1)
threshold2.Scalars = ['CELLS', 'SeparatrixType']
threshold2.LowerThreshold = 2.0
threshold2.UpperThreshold = 2.0

# create a new 'Threshold'
threshold3 = Threshold(registrationName='Threshold3', Input=threshold2)
threshold3.Scalars = ['CELLS', 'NumberOfCriticalPointsOnBoundary']
threshold3.LowerThreshold = 1.0
threshold3.UpperThreshold = 1.0

SaveData("liH_toroidalVortex.vtu", tTKGeometrySmoother2)
SaveData("liH_axialVortex.vtu", threshold3)
