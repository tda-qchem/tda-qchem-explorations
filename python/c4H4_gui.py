# state file generated using paraview version 5.10.1

# uncomment the following three lines to ensure this script works in future versions
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1377, 564]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [0.009735928741464214, -22.72252163658303, 8.07411139836411]
renderView1.CameraFocalPoint = [0.397099466392463, -0.34448408855139523, -0.8468847931355686]
renderView1.CameraViewUp = [0.00934034978436339, 0.37015339572619144, 0.9289236898143332]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 9.130028194507704
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView2 = CreateView('RenderView')
renderView2.ViewSize = [684, 563]
renderView2.AxesGrid = 'GridAxes3DActor'
renderView2.OrientationAxesVisibility = 0
renderView2.StereoType = 'Crystal Eyes'
renderView2.CameraPosition = [0.009735928741464214, -22.72252163658303, 8.07411139836411]
renderView2.CameraFocalPoint = [0.397099466392463, -0.34448408855139523, -0.8468847931355686]
renderView2.CameraViewUp = [0.00934034978436339, 0.37015339572619144, 0.9289236898143332]
renderView2.CameraFocalDisk = 1.0
renderView2.CameraParallelScale = 9.130028194507704
renderView2.BackEnd = 'OSPRay raycaster'
renderView2.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView3 = CreateView('RenderView')
renderView3.ViewSize = [683, 563]
renderView3.AxesGrid = 'GridAxes3DActor'
renderView3.OrientationAxesVisibility = 0
renderView3.StereoType = 'Crystal Eyes'
renderView3.CameraPosition = [0.009735928741464214, -22.72252163658303, 8.07411139836411]
renderView3.CameraFocalPoint = [0.397099466392463, -0.34448408855139523, -0.8468847931355686]
renderView3.CameraViewUp = [0.00934034978436339, 0.37015339572619144, 0.9289236898143332]
renderView3.CameraFocalDisk = 1.0
renderView3.CameraParallelScale = 9.130028194507704
renderView3.BackEnd = 'OSPRay raycaster'
renderView3.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.SplitVertical(0, 0.500000)
layout1.AssignView(1, renderView1)
layout1.SplitHorizontal(2, 0.500000)
layout1.AssignView(5, renderView2)
layout1.AssignView(6, renderView3)
layout1.SetSize(1377, 1128)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView3)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'XML Image Data Reader'
start_data_omega_bzvti = XMLImageDataReader(registrationName='start_data_omega_bz.vti', FileName=['data/C4H4_MICD/vti/start_data_omega_bz.vti'])
start_data_omega_bzvti.CellArrayStatus = ['vtkGhostType']
start_data_omega_bzvti.PointArrayStatus = ['bz_wz', 'omega_bz', 'vtkValidPointMask', 'vtkGhostType']
start_data_omega_bzvti.TimeArray = 'None'

# create a new 'TTK PersistentGenerators'
tTKPersistentGenerators2 = TTKPersistentGenerators(registrationName='TTKPersistentGenerators2', Input=start_data_omega_bzvti)
tTKPersistentGenerators2.ScalarField = ['POINTS', 'omega_bz']
tTKPersistentGenerators2.InputOffsetField = ['POINTS', 'bz_wz']

# create a new 'Threshold'
threshold2 = Threshold(registrationName='Threshold2', Input=tTKPersistentGenerators2)
threshold2.Scalars = ['CELLS', 'ComponentId']

# create a new 'Threshold'
threshold3 = Threshold(registrationName='Threshold3', Input=threshold2)
threshold3.Scalars = ['CELLS', 'Persistence']
threshold3.LowerThreshold = 0.4
threshold3.UpperThreshold = 0.9227403150404694

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=start_data_omega_bzvti)
calculator1.ResultArrayName = 'oppositeOmega'
calculator1.Function = '-omega_bz'

# create a new 'TTK PersistentGenerators'
tTKPersistentGenerators1 = TTKPersistentGenerators(registrationName='TTKPersistentGenerators1', Input=calculator1)
tTKPersistentGenerators1.ScalarField = ['POINTS', 'oppositeOmega']
tTKPersistentGenerators1.InputOffsetField = ['POINTS', 'oppositeOmega']

# create a new 'Threshold'
threshold1 = Threshold(registrationName='Threshold1', Input=tTKPersistentGenerators1)
threshold1.Scalars = ['CELLS', 'Persistence']
threshold1.LowerThreshold = 0.5
threshold1.UpperThreshold = 0.5377742050554125

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother1 = TTKGeometrySmoother(registrationName='TTKGeometrySmoother1', Input=threshold1)
tTKGeometrySmoother1.IterationNumber = 10
tTKGeometrySmoother1.InputMaskField = ['POINTS', 'oppositeOmega']

# create a new 'TTK TopologicalSimplificationByPersistence'
tTKTopologicalSimplificationByPersistence1 = TTKTopologicalSimplificationByPersistence(registrationName='TTKTopologicalSimplificationByPersistence1', Input=start_data_omega_bzvti)
tTKTopologicalSimplificationByPersistence1.InputArray = ['POINTS', 'omega_bz']
tTKTopologicalSimplificationByPersistence1.PersistenceThreshold = 0.1

# create a new 'TTK MorseSmaleComplex'
tTKMorseSmaleComplex1 = TTKMorseSmaleComplex(registrationName='TTKMorseSmaleComplex1', Input=tTKTopologicalSimplificationByPersistence1)
tTKMorseSmaleComplex1.ScalarField = ['POINTS', 'omega_bz']
tTKMorseSmaleComplex1.OffsetField = ['POINTS', 'bz_wz']
tTKMorseSmaleComplex1.AscendingSegmentation = 0
tTKMorseSmaleComplex1.DescendingSegmentation = 0
tTKMorseSmaleComplex1.MorseSmaleComplexSegmentation = 0
tTKMorseSmaleComplex1.ReturnSaddleConnectors = 1
tTKMorseSmaleComplex1.SaddleConnectorsPersistenceThreshold = 0.4

# find source
tTKMorseSmaleComplex1_1 = FindSource('TTKMorseSmaleComplex1')

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother3 = TTKGeometrySmoother(registrationName='TTKGeometrySmoother3', Input=OutputPort(tTKMorseSmaleComplex1_1,1))
tTKGeometrySmoother3.IterationNumber = 100
tTKGeometrySmoother3.InputMaskField = ['CELLS', 'SeparatrixType']

# create a new 'Threshold'
threshold4 = Threshold(registrationName='Threshold4', Input=tTKGeometrySmoother3)
threshold4.Scalars = ['CELLS', 'SeparatrixType']
threshold4.LowerThreshold = 2.0
threshold4.UpperThreshold = 2.0

# create a new 'Threshold'
threshold5 = Threshold(registrationName='Threshold5', Input=threshold4)
threshold5.Scalars = ['CELLS', 'NumberOfCriticalPointsOnBoundary']
threshold5.LowerThreshold = 1.0
threshold5.UpperThreshold = 1.0

# create a new 'Threshold'
threshold6 = Threshold(registrationName='Threshold6', Input=threshold5)
threshold6.Scalars = ['CELLS', 'SeparatrixFunctionMaximum']
threshold6.LowerThreshold = 0.99
threshold6.UpperThreshold = 0.9999551958395428

# create a new 'Contour'
contour1 = Contour(registrationName='Contour1', Input=start_data_omega_bzvti)
contour1.ContourBy = ['POINTS', 'omega_bz']
contour1.Isosurfaces = [0.5]
contour1.PointMergeMethod = 'Uniform Binning'

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother2 = TTKGeometrySmoother(registrationName='TTKGeometrySmoother2', Input=threshold3)
tTKGeometrySmoother2.IterationNumber = 10
tTKGeometrySmoother2.InputMaskField = ['POINTS', 'omega_bz']

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from contour1
contour1Display = Show(contour1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
contour1Display.Representation = 'Surface'
contour1Display.ColorArrayName = ['POINTS', '']
contour1Display.Opacity = 0.2
contour1Display.Specular = 1.0
contour1Display.SelectTCoordArray = 'None'
contour1Display.SelectNormalArray = 'Normals'
contour1Display.SelectTangentArray = 'None'
contour1Display.OSPRayScaleArray = 'omega_bz'
contour1Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display.SelectOrientationVectors = 'None'
contour1Display.ScaleFactor = 1.1557316780090332
contour1Display.SelectScaleArray = 'omega_bz'
contour1Display.GlyphType = 'Arrow'
contour1Display.GlyphTableIndexArray = 'omega_bz'
contour1Display.GaussianRadius = 0.05778658390045166
contour1Display.SetScaleArray = ['POINTS', 'omega_bz']
contour1Display.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display.OpacityArray = ['POINTS', 'omega_bz']
contour1Display.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display.DataAxesGrid = 'GridAxesRepresentation'
contour1Display.PolarAxes = 'PolarAxesRepresentation'
contour1Display.SelectInputVectors = ['POINTS', 'Normals']
contour1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
contour1Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour1Display.ScaleTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5001220703125, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour1Display.OpacityTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5001220703125, 1.0, 0.5, 0.0]

# show data from tTKMorseSmaleComplex1
tTKMorseSmaleComplex1Display = Show(tTKMorseSmaleComplex1, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'CellDimension'
cellDimensionLUT = GetColorTransferFunction('CellDimension')
cellDimensionLUT.RGBPoints = [0.0, 0.0, 0.129412, 0.584314, 1.5000000000000013, 0.917647, 0.941176, 0.788235, 3.0, 0.0, 0.431373, 0.0]
cellDimensionLUT.ColorSpace = 'RGB'
cellDimensionLUT.AboveRangeColor = [1.0, 1.0, 1.0]
cellDimensionLUT.NanColor = [0.0, 0.0, 0.0]
cellDimensionLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
tTKMorseSmaleComplex1Display.Representation = 'Surface'
tTKMorseSmaleComplex1Display.ColorArrayName = ['POINTS', 'CellDimension']
tTKMorseSmaleComplex1Display.LookupTable = cellDimensionLUT
tTKMorseSmaleComplex1Display.PointSize = 20.0
tTKMorseSmaleComplex1Display.RenderPointsAsSpheres = 1
tTKMorseSmaleComplex1Display.Specular = 1.0
tTKMorseSmaleComplex1Display.SelectTCoordArray = 'None'
tTKMorseSmaleComplex1Display.SelectNormalArray = 'None'
tTKMorseSmaleComplex1Display.SelectTangentArray = 'None'
tTKMorseSmaleComplex1Display.OSPRayScaleArray = 'CellDimension'
tTKMorseSmaleComplex1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1Display.SelectOrientationVectors = 'None'
tTKMorseSmaleComplex1Display.ScaleFactor = 1.1321261405944825
tTKMorseSmaleComplex1Display.SelectScaleArray = 'CellDimension'
tTKMorseSmaleComplex1Display.GlyphType = 'Arrow'
tTKMorseSmaleComplex1Display.GlyphTableIndexArray = 'CellDimension'
tTKMorseSmaleComplex1Display.GaussianRadius = 0.05660630702972412
tTKMorseSmaleComplex1Display.SetScaleArray = ['POINTS', 'CellDimension']
tTKMorseSmaleComplex1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1Display.OpacityArray = ['POINTS', 'CellDimension']
tTKMorseSmaleComplex1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKMorseSmaleComplex1Display.PolarAxes = 'PolarAxesRepresentation'
tTKMorseSmaleComplex1Display.SelectInputVectors = ['POINTS', 'CellDimension']
tTKMorseSmaleComplex1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKMorseSmaleComplex1Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKMorseSmaleComplex1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKMorseSmaleComplex1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# find source
tTKMorseSmaleComplex1_2 = FindSource('TTKMorseSmaleComplex1')

# show data from tTKMorseSmaleComplex1_2
tTKMorseSmaleComplex1_2Display = Show(OutputPort(tTKMorseSmaleComplex1_2, 2), renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
tTKMorseSmaleComplex1_2Display.Representation = 'Surface'
tTKMorseSmaleComplex1_2Display.ColorArrayName = [None, '']
tTKMorseSmaleComplex1_2Display.Specular = 1.0
tTKMorseSmaleComplex1_2Display.SelectTCoordArray = 'None'
tTKMorseSmaleComplex1_2Display.SelectNormalArray = 'None'
tTKMorseSmaleComplex1_2Display.SelectTangentArray = 'None'
tTKMorseSmaleComplex1_2Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1_2Display.SelectOrientationVectors = 'None'
tTKMorseSmaleComplex1_2Display.ScaleFactor = -0.2
tTKMorseSmaleComplex1_2Display.SelectScaleArray = 'None'
tTKMorseSmaleComplex1_2Display.GlyphType = 'Arrow'
tTKMorseSmaleComplex1_2Display.GlyphTableIndexArray = 'None'
tTKMorseSmaleComplex1_2Display.GaussianRadius = -0.01
tTKMorseSmaleComplex1_2Display.SetScaleArray = [None, '']
tTKMorseSmaleComplex1_2Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1_2Display.OpacityArray = [None, '']
tTKMorseSmaleComplex1_2Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1_2Display.DataAxesGrid = 'GridAxesRepresentation'
tTKMorseSmaleComplex1_2Display.PolarAxes = 'PolarAxesRepresentation'
tTKMorseSmaleComplex1_2Display.SelectInputVectors = [None, '']
tTKMorseSmaleComplex1_2Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKMorseSmaleComplex1_2Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# find source
tTKMorseSmaleComplex1_3 = FindSource('TTKMorseSmaleComplex1')

# show data from tTKMorseSmaleComplex1_3
tTKMorseSmaleComplex1_3Display = Show(OutputPort(tTKMorseSmaleComplex1_3, 3), renderView1, 'UniformGridRepresentation')

# trace defaults for the display properties.
tTKMorseSmaleComplex1_3Display.Representation = 'Outline'
tTKMorseSmaleComplex1_3Display.ColorArrayName = [None, '']
tTKMorseSmaleComplex1_3Display.SelectTCoordArray = 'None'
tTKMorseSmaleComplex1_3Display.SelectNormalArray = 'None'
tTKMorseSmaleComplex1_3Display.SelectTangentArray = 'None'
tTKMorseSmaleComplex1_3Display.OSPRayScaleArray = 'bz_wz'
tTKMorseSmaleComplex1_3Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1_3Display.SelectOrientationVectors = 'None'
tTKMorseSmaleComplex1_3Display.ScaleFactor = 1.1557316422672022
tTKMorseSmaleComplex1_3Display.SelectScaleArray = 'None'
tTKMorseSmaleComplex1_3Display.GlyphType = 'Arrow'
tTKMorseSmaleComplex1_3Display.GlyphTableIndexArray = 'None'
tTKMorseSmaleComplex1_3Display.GaussianRadius = 0.0577865821133601
tTKMorseSmaleComplex1_3Display.SetScaleArray = ['POINTS', 'bz_wz']
tTKMorseSmaleComplex1_3Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1_3Display.OpacityArray = ['POINTS', 'bz_wz']
tTKMorseSmaleComplex1_3Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1_3Display.DataAxesGrid = 'GridAxesRepresentation'
tTKMorseSmaleComplex1_3Display.PolarAxes = 'PolarAxesRepresentation'
tTKMorseSmaleComplex1_3Display.ScalarOpacityUnitDistance = 0.14377997350161018
tTKMorseSmaleComplex1_3Display.OpacityArrayName = ['POINTS', 'bz_wz']
tTKMorseSmaleComplex1_3Display.SliceFunction = 'Plane'
tTKMorseSmaleComplex1_3Display.Slice = 63
tTKMorseSmaleComplex1_3Display.SelectInputVectors = ['POINTS', 'bz_wz']
tTKMorseSmaleComplex1_3Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKMorseSmaleComplex1_3Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKMorseSmaleComplex1_3Display.ScaleTransferFunction.Points = [-4.988074235242512, 0.0, 0.5, 0.0, 41.39895776262771, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKMorseSmaleComplex1_3Display.OpacityTransferFunction.Points = [-4.988074235242512, 0.0, 0.5, 0.0, 41.39895776262771, 1.0, 0.5, 0.0]

# show data from tTKGeometrySmoother3
tTKGeometrySmoother3Display = Show(tTKGeometrySmoother3, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'SeparatrixType'
separatrixTypeLUT = GetColorTransferFunction('SeparatrixType')
separatrixTypeLUT.RGBPoints = [0.0, 0.0, 0.129412, 0.584314, 1.0002441406250009, 0.917647, 0.941176, 0.788235, 2.00048828125, 0.0, 0.431373, 0.0]
separatrixTypeLUT.ColorSpace = 'RGB'
separatrixTypeLUT.AboveRangeColor = [1.0, 1.0, 1.0]
separatrixTypeLUT.NanColor = [0.0, 0.0, 0.0]
separatrixTypeLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
tTKGeometrySmoother3Display.Representation = 'Surface'
tTKGeometrySmoother3Display.ColorArrayName = ['CELLS', 'SeparatrixType']
tTKGeometrySmoother3Display.LookupTable = separatrixTypeLUT
tTKGeometrySmoother3Display.LineWidth = 5.0
tTKGeometrySmoother3Display.RenderLinesAsTubes = 1
tTKGeometrySmoother3Display.Specular = 1.0
tTKGeometrySmoother3Display.SelectTCoordArray = 'None'
tTKGeometrySmoother3Display.SelectNormalArray = 'None'
tTKGeometrySmoother3Display.SelectTangentArray = 'None'
tTKGeometrySmoother3Display.OSPRayScaleArray = 'CellDimension'
tTKGeometrySmoother3Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKGeometrySmoother3Display.SelectOrientationVectors = 'None'
tTKGeometrySmoother3Display.ScaleFactor = 1.1321261405944825
tTKGeometrySmoother3Display.SelectScaleArray = 'SeparatrixType'
tTKGeometrySmoother3Display.GlyphType = 'Arrow'
tTKGeometrySmoother3Display.GlyphTableIndexArray = 'SeparatrixType'
tTKGeometrySmoother3Display.GaussianRadius = 0.05660630702972412
tTKGeometrySmoother3Display.SetScaleArray = ['POINTS', 'CellDimension']
tTKGeometrySmoother3Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKGeometrySmoother3Display.OpacityArray = ['POINTS', 'CellDimension']
tTKGeometrySmoother3Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKGeometrySmoother3Display.DataAxesGrid = 'GridAxesRepresentation'
tTKGeometrySmoother3Display.PolarAxes = 'PolarAxesRepresentation'
tTKGeometrySmoother3Display.SelectInputVectors = ['POINTS', 'CellDimension']
tTKGeometrySmoother3Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKGeometrySmoother3Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKGeometrySmoother3Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKGeometrySmoother3Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# ----------------------------------------------------------------
# setup the visualization in view 'renderView2'
# ----------------------------------------------------------------

# show data from start_data_omega_bzvti
start_data_omega_bzvtiDisplay = Show(start_data_omega_bzvti, renderView2, 'UniformGridRepresentation')

# trace defaults for the display properties.
start_data_omega_bzvtiDisplay.Representation = 'Outline'
start_data_omega_bzvtiDisplay.ColorArrayName = [None, '']
start_data_omega_bzvtiDisplay.SelectTCoordArray = 'None'
start_data_omega_bzvtiDisplay.SelectNormalArray = 'None'
start_data_omega_bzvtiDisplay.SelectTangentArray = 'None'
start_data_omega_bzvtiDisplay.OSPRayScaleArray = 'bz_wz'
start_data_omega_bzvtiDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay.SelectOrientationVectors = 'None'
start_data_omega_bzvtiDisplay.ScaleFactor = 1.1557316422672022
start_data_omega_bzvtiDisplay.SelectScaleArray = 'None'
start_data_omega_bzvtiDisplay.GlyphType = 'Arrow'
start_data_omega_bzvtiDisplay.GlyphTableIndexArray = 'None'
start_data_omega_bzvtiDisplay.GaussianRadius = 0.0577865821133601
start_data_omega_bzvtiDisplay.SetScaleArray = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay.ScaleTransferFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay.OpacityArray = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay.OpacityTransferFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay.DataAxesGrid = 'GridAxesRepresentation'
start_data_omega_bzvtiDisplay.PolarAxes = 'PolarAxesRepresentation'
start_data_omega_bzvtiDisplay.ScalarOpacityUnitDistance = 0.14377997350161018
start_data_omega_bzvtiDisplay.OpacityArrayName = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay.SliceFunction = 'Plane'
start_data_omega_bzvtiDisplay.Slice = 63
start_data_omega_bzvtiDisplay.SelectInputVectors = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
start_data_omega_bzvtiDisplay.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
start_data_omega_bzvtiDisplay.ScaleTransferFunction.Points = [-4.988074235242512, 0.0, 0.5, 0.0, 41.39895776262771, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
start_data_omega_bzvtiDisplay.OpacityTransferFunction.Points = [-4.988074235242512, 0.0, 0.5, 0.0, 41.39895776262771, 1.0, 0.5, 0.0]

# show data from contour1
contour1Display_1 = Show(contour1, renderView2, 'GeometryRepresentation')

# trace defaults for the display properties.
contour1Display_1.Representation = 'Surface'
contour1Display_1.ColorArrayName = ['POINTS', '']
contour1Display_1.Opacity = 0.2
contour1Display_1.Specular = 1.0
contour1Display_1.SelectTCoordArray = 'None'
contour1Display_1.SelectNormalArray = 'Normals'
contour1Display_1.SelectTangentArray = 'None'
contour1Display_1.OSPRayScaleArray = 'omega_bz'
contour1Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display_1.SelectOrientationVectors = 'None'
contour1Display_1.ScaleFactor = 1.1557316780090332
contour1Display_1.SelectScaleArray = 'omega_bz'
contour1Display_1.GlyphType = 'Arrow'
contour1Display_1.GlyphTableIndexArray = 'omega_bz'
contour1Display_1.GaussianRadius = 0.05778658390045166
contour1Display_1.SetScaleArray = ['POINTS', 'omega_bz']
contour1Display_1.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display_1.OpacityArray = ['POINTS', 'omega_bz']
contour1Display_1.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display_1.DataAxesGrid = 'GridAxesRepresentation'
contour1Display_1.PolarAxes = 'PolarAxesRepresentation'
contour1Display_1.SelectInputVectors = ['POINTS', 'Normals']
contour1Display_1.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
contour1Display_1.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour1Display_1.ScaleTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5001220703125, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour1Display_1.OpacityTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5001220703125, 1.0, 0.5, 0.0]

# show data from tTKGeometrySmoother1
tTKGeometrySmoother1Display = Show(tTKGeometrySmoother1, renderView2, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'Persistence'
persistenceLUT = GetColorTransferFunction('Persistence')
persistenceLUT.RGBPoints = [0.45003952120704216, 0.0, 0.129412, 0.584314, 0.6863899181237567, 0.917647, 0.941176, 0.788235, 0.9227403150404694, 0.0, 0.431373, 0.0]
persistenceLUT.ColorSpace = 'RGB'
persistenceLUT.AboveRangeColor = [1.0, 1.0, 1.0]
persistenceLUT.NanColor = [0.0, 0.0, 0.0]
persistenceLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'Persistence'
persistencePWF = GetOpacityTransferFunction('Persistence')
persistencePWF.Points = [0.45003952120704216, 0.0, 0.5, 0.0, 0.9227403150404694, 1.0, 0.5, 0.0]
persistencePWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
tTKGeometrySmoother1Display.Representation = 'Surface'
tTKGeometrySmoother1Display.ColorArrayName = ['CELLS', 'Persistence']
tTKGeometrySmoother1Display.LookupTable = persistenceLUT
tTKGeometrySmoother1Display.LineWidth = 10.0
tTKGeometrySmoother1Display.RenderLinesAsTubes = 1
tTKGeometrySmoother1Display.Specular = 1.0
tTKGeometrySmoother1Display.SelectTCoordArray = 'None'
tTKGeometrySmoother1Display.SelectNormalArray = 'None'
tTKGeometrySmoother1Display.SelectTangentArray = 'None'
tTKGeometrySmoother1Display.OSPRayScaleArray = 'oppositeOmega'
tTKGeometrySmoother1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKGeometrySmoother1Display.SelectOrientationVectors = 'None'
tTKGeometrySmoother1Display.ScaleFactor = 0.3113550186157227
tTKGeometrySmoother1Display.SelectScaleArray = 'None'
tTKGeometrySmoother1Display.GlyphType = 'Arrow'
tTKGeometrySmoother1Display.GlyphTableIndexArray = 'None'
tTKGeometrySmoother1Display.GaussianRadius = 0.015567750930786134
tTKGeometrySmoother1Display.SetScaleArray = ['POINTS', 'oppositeOmega']
tTKGeometrySmoother1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKGeometrySmoother1Display.OpacityArray = ['POINTS', 'oppositeOmega']
tTKGeometrySmoother1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKGeometrySmoother1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKGeometrySmoother1Display.PolarAxes = 'PolarAxesRepresentation'
tTKGeometrySmoother1Display.ScalarOpacityFunction = persistencePWF
tTKGeometrySmoother1Display.ScalarOpacityUnitDistance = 0.8683407699650976
tTKGeometrySmoother1Display.OpacityArrayName = ['POINTS', 'oppositeOmega']
tTKGeometrySmoother1Display.SelectInputVectors = ['POINTS', 'oppositeOmega']
tTKGeometrySmoother1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKGeometrySmoother1Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKGeometrySmoother1Display.ScaleTransferFunction.Points = [-0.9825829749269096, 0.0, 0.5, 0.0, -0.6905705066567652, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKGeometrySmoother1Display.OpacityTransferFunction.Points = [-0.9825829749269096, 0.0, 0.5, 0.0, -0.6905705066567652, 1.0, 0.5, 0.0]

# show data from tTKGeometrySmoother2
tTKGeometrySmoother2Display = Show(tTKGeometrySmoother2, renderView2, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
tTKGeometrySmoother2Display.Representation = 'Surface'
tTKGeometrySmoother2Display.ColorArrayName = ['CELLS', 'Persistence']
tTKGeometrySmoother2Display.LookupTable = persistenceLUT
tTKGeometrySmoother2Display.LineWidth = 10.0
tTKGeometrySmoother2Display.RenderLinesAsTubes = 1
tTKGeometrySmoother2Display.Specular = 1.0
tTKGeometrySmoother2Display.SelectTCoordArray = 'None'
tTKGeometrySmoother2Display.SelectNormalArray = 'None'
tTKGeometrySmoother2Display.SelectTangentArray = 'None'
tTKGeometrySmoother2Display.OSPRayScaleArray = 'omega_bz'
tTKGeometrySmoother2Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKGeometrySmoother2Display.SelectOrientationVectors = 'None'
tTKGeometrySmoother2Display.ScaleFactor = 1.1557316780090332
tTKGeometrySmoother2Display.SelectScaleArray = 'None'
tTKGeometrySmoother2Display.GlyphType = 'Arrow'
tTKGeometrySmoother2Display.GlyphTableIndexArray = 'None'
tTKGeometrySmoother2Display.GaussianRadius = 0.05778658390045166
tTKGeometrySmoother2Display.SetScaleArray = ['POINTS', 'omega_bz']
tTKGeometrySmoother2Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKGeometrySmoother2Display.OpacityArray = ['POINTS', 'omega_bz']
tTKGeometrySmoother2Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKGeometrySmoother2Display.DataAxesGrid = 'GridAxesRepresentation'
tTKGeometrySmoother2Display.PolarAxes = 'PolarAxesRepresentation'
tTKGeometrySmoother2Display.ScalarOpacityFunction = persistencePWF
tTKGeometrySmoother2Display.ScalarOpacityUnitDistance = 1.3414160715726524
tTKGeometrySmoother2Display.OpacityArrayName = ['POINTS', 'omega_bz']
tTKGeometrySmoother2Display.SelectInputVectors = ['POINTS', 'omega_bz']
tTKGeometrySmoother2Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKGeometrySmoother2Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKGeometrySmoother2Display.ScaleTransferFunction.Points = [0.010953966923222832, 0.0, 0.5, 0.0, 0.25444463390487426, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKGeometrySmoother2Display.OpacityTransferFunction.Points = [0.010953966923222832, 0.0, 0.5, 0.0, 0.25444463390487426, 1.0, 0.5, 0.0]

# ----------------------------------------------------------------
# setup the visualization in view 'renderView3'
# ----------------------------------------------------------------

# show data from contour1
contour1Display_2 = Show(contour1, renderView3, 'GeometryRepresentation')

# trace defaults for the display properties.
contour1Display_2.Representation = 'Surface'
contour1Display_2.ColorArrayName = ['POINTS', '']
contour1Display_2.Opacity = 0.2
contour1Display_2.Specular = 1.0
contour1Display_2.SelectTCoordArray = 'None'
contour1Display_2.SelectNormalArray = 'Normals'
contour1Display_2.SelectTangentArray = 'None'
contour1Display_2.OSPRayScaleArray = 'omega_bz'
contour1Display_2.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display_2.SelectOrientationVectors = 'None'
contour1Display_2.ScaleFactor = 1.1557316780090332
contour1Display_2.SelectScaleArray = 'omega_bz'
contour1Display_2.GlyphType = 'Arrow'
contour1Display_2.GlyphTableIndexArray = 'omega_bz'
contour1Display_2.GaussianRadius = 0.05778658390045166
contour1Display_2.SetScaleArray = ['POINTS', 'omega_bz']
contour1Display_2.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display_2.OpacityArray = ['POINTS', 'omega_bz']
contour1Display_2.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display_2.DataAxesGrid = 'GridAxesRepresentation'
contour1Display_2.PolarAxes = 'PolarAxesRepresentation'
contour1Display_2.SelectInputVectors = ['POINTS', 'Normals']
contour1Display_2.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
contour1Display_2.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour1Display_2.ScaleTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5001220703125, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour1Display_2.OpacityTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5001220703125, 1.0, 0.5, 0.0]

# show data from start_data_omega_bzvti
start_data_omega_bzvtiDisplay_1 = Show(start_data_omega_bzvti, renderView3, 'UniformGridRepresentation')

# trace defaults for the display properties.
start_data_omega_bzvtiDisplay_1.Representation = 'Outline'
start_data_omega_bzvtiDisplay_1.ColorArrayName = [None, '']
start_data_omega_bzvtiDisplay_1.SelectTCoordArray = 'None'
start_data_omega_bzvtiDisplay_1.SelectNormalArray = 'None'
start_data_omega_bzvtiDisplay_1.SelectTangentArray = 'None'
start_data_omega_bzvtiDisplay_1.OSPRayScaleArray = 'bz_wz'
start_data_omega_bzvtiDisplay_1.OSPRayScaleFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay_1.SelectOrientationVectors = 'None'
start_data_omega_bzvtiDisplay_1.ScaleFactor = 1.1557316422672022
start_data_omega_bzvtiDisplay_1.SelectScaleArray = 'None'
start_data_omega_bzvtiDisplay_1.GlyphType = 'Arrow'
start_data_omega_bzvtiDisplay_1.GlyphTableIndexArray = 'None'
start_data_omega_bzvtiDisplay_1.GaussianRadius = 0.0577865821133601
start_data_omega_bzvtiDisplay_1.SetScaleArray = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_1.ScaleTransferFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay_1.OpacityArray = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_1.OpacityTransferFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay_1.DataAxesGrid = 'GridAxesRepresentation'
start_data_omega_bzvtiDisplay_1.PolarAxes = 'PolarAxesRepresentation'
start_data_omega_bzvtiDisplay_1.ScalarOpacityUnitDistance = 0.14377997350161018
start_data_omega_bzvtiDisplay_1.OpacityArrayName = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_1.SliceFunction = 'Plane'
start_data_omega_bzvtiDisplay_1.Slice = 63
start_data_omega_bzvtiDisplay_1.SelectInputVectors = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_1.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
start_data_omega_bzvtiDisplay_1.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
start_data_omega_bzvtiDisplay_1.ScaleTransferFunction.Points = [-4.988074235242512, 0.0, 0.5, 0.0, 41.39895776262771, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
start_data_omega_bzvtiDisplay_1.OpacityTransferFunction.Points = [-4.988074235242512, 0.0, 0.5, 0.0, 41.39895776262771, 1.0, 0.5, 0.0]

# show data from threshold5
threshold5Display = Show(threshold5, renderView3, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'SeparatrixFunctionMaximum'
separatrixFunctionMaximumLUT = GetColorTransferFunction('SeparatrixFunctionMaximum')
separatrixFunctionMaximumLUT.RGBPoints = [0.9841607110030205, 0.0, 0.129412, 0.584314, 0.9920579534212817, 0.917647, 0.941176, 0.788235, 0.9999551958395428, 0.0, 0.431373, 0.0]
separatrixFunctionMaximumLUT.ColorSpace = 'RGB'
separatrixFunctionMaximumLUT.AboveRangeColor = [1.0, 1.0, 1.0]
separatrixFunctionMaximumLUT.NanColor = [0.0, 0.0, 0.0]
separatrixFunctionMaximumLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'SeparatrixFunctionMaximum'
separatrixFunctionMaximumPWF = GetOpacityTransferFunction('SeparatrixFunctionMaximum')
separatrixFunctionMaximumPWF.Points = [0.9841607110030205, 0.0, 0.5, 0.0, 0.9999551958395428, 1.0, 0.5, 0.0]
separatrixFunctionMaximumPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
threshold5Display.Representation = 'Surface'
threshold5Display.ColorArrayName = ['CELLS', 'SeparatrixFunctionMaximum']
threshold5Display.LookupTable = separatrixFunctionMaximumLUT
threshold5Display.Opacity = 0.3
threshold5Display.LineWidth = 5.0
threshold5Display.RenderLinesAsTubes = 1
threshold5Display.Specular = 1.0
threshold5Display.SelectTCoordArray = 'None'
threshold5Display.SelectNormalArray = 'None'
threshold5Display.SelectTangentArray = 'None'
threshold5Display.OSPRayScaleArray = 'CellDimension'
threshold5Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold5Display.SelectOrientationVectors = 'None'
threshold5Display.ScaleFactor = 1.1557316780090332
threshold5Display.SelectScaleArray = 'SeparatrixType'
threshold5Display.GlyphType = 'Arrow'
threshold5Display.GlyphTableIndexArray = 'SeparatrixType'
threshold5Display.GaussianRadius = 0.05778658390045166
threshold5Display.SetScaleArray = ['POINTS', 'CellDimension']
threshold5Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold5Display.OpacityArray = ['POINTS', 'CellDimension']
threshold5Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold5Display.DataAxesGrid = 'GridAxesRepresentation'
threshold5Display.PolarAxes = 'PolarAxesRepresentation'
threshold5Display.ScalarOpacityFunction = separatrixFunctionMaximumPWF
threshold5Display.ScalarOpacityUnitDistance = 1.1164763908694249
threshold5Display.OpacityArrayName = ['CELLS', 'SeparatrixType']
threshold5Display.SelectInputVectors = ['POINTS', 'CellDimension']
threshold5Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
threshold5Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold5Display.ScaleTransferFunction.Points = [2.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold5Display.OpacityTransferFunction.Points = [2.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# show data from threshold6
threshold6Display = Show(threshold6, renderView3, 'UnstructuredGridRepresentation')

# get opacity transfer function/opacity map for 'SeparatrixType'
separatrixTypePWF = GetOpacityTransferFunction('SeparatrixType')
separatrixTypePWF.Points = [0.0, 0.0, 0.5, 0.0, 2.00048828125, 1.0, 0.5, 0.0]
separatrixTypePWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
threshold6Display.Representation = 'Surface'
threshold6Display.ColorArrayName = ['CELLS', 'SeparatrixType']
threshold6Display.LookupTable = separatrixTypeLUT
threshold6Display.LineWidth = 10.0
threshold6Display.RenderLinesAsTubes = 1
threshold6Display.Specular = 1.0
threshold6Display.SelectTCoordArray = 'None'
threshold6Display.SelectNormalArray = 'None'
threshold6Display.SelectTangentArray = 'None'
threshold6Display.OSPRayScaleArray = 'CellDimension'
threshold6Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold6Display.SelectOrientationVectors = 'None'
threshold6Display.ScaleFactor = 1.1557316780090332
threshold6Display.SelectScaleArray = 'SeparatrixType'
threshold6Display.GlyphType = 'Arrow'
threshold6Display.GlyphTableIndexArray = 'SeparatrixType'
threshold6Display.GaussianRadius = 0.05778658390045166
threshold6Display.SetScaleArray = ['POINTS', 'CellDimension']
threshold6Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold6Display.OpacityArray = ['POINTS', 'CellDimension']
threshold6Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold6Display.DataAxesGrid = 'GridAxesRepresentation'
threshold6Display.PolarAxes = 'PolarAxesRepresentation'
threshold6Display.ScalarOpacityFunction = separatrixTypePWF
threshold6Display.ScalarOpacityUnitDistance = 1.1164763908694249
threshold6Display.OpacityArrayName = ['CELLS', 'SeparatrixType']
threshold6Display.SelectInputVectors = ['POINTS', 'CellDimension']
threshold6Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
threshold6Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold6Display.ScaleTransferFunction.Points = [2.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold6Display.OpacityTransferFunction.Points = [2.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'CellDimension'
cellDimensionPWF = GetOpacityTransferFunction('CellDimension')
cellDimensionPWF.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]
cellDimensionPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# restore active source
SetActiveSource(threshold5)
# ----------------------------------------------------------------


if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')
