#!/usr/bin/env python

from paraview.simple import *

# create a new 'XML Image Data Reader'
start_data_allvti = XMLImageDataReader(FileName=['data/H2O_ED_basins/vti/start_data_all.vti'])

# create a new 'TTK TopologicalSimplificationByPersistence'
tTKTopologicalSimplificationByPersistence1 = TTKTopologicalSimplificationByPersistence(Input=start_data_allvti)
tTKTopologicalSimplificationByPersistence1.InputArray = ['POINTS', 'rho']

# create a new 'TTK MorseSmaleComplex'
tTKMorseSmaleComplex1 = TTKMorseSmaleComplex(Input=tTKTopologicalSimplificationByPersistence1)
tTKMorseSmaleComplex1.ScalarField = ['POINTS', 'rho']
tTKMorseSmaleComplex1.AscendingSegmentation = 0
tTKMorseSmaleComplex1.DescendingSegmentation = 0
tTKMorseSmaleComplex1.MorseSmaleComplexSegmentation = 0

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother1 = TTKGeometrySmoother(Input=OutputPort(tTKMorseSmaleComplex1,1))
tTKGeometrySmoother1.IterationNumber = 1000

# create a new 'Threshold'
threshold1 = Threshold(Input=tTKGeometrySmoother1)
threshold1.Scalars = ['CELLS', 'SeparatrixType']
threshold1.LowerThreshold = 2.0
threshold1.UpperThreshold = 2.0

# create a new 'Threshold'
threshold2 = Threshold(Input=threshold1)
threshold2.Scalars = ['CELLS', 'NumberOfCriticalPointsOnBoundary']

SaveData("h2O_covalentBonds.vtu", threshold2)
