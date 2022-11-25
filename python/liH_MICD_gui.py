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
renderView1.CenterOfRotation = [0.0, -1e-20, 0.0]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [0.0, 20.636890206955403, 0.0]
renderView1.CameraFocalPoint = [0.0, -1e-20, 0.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 7.820080520075376
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView2 = CreateView('RenderView')
renderView2.ViewSize = [684, 563]
renderView2.AxesGrid = 'GridAxes3DActor'
renderView2.OrientationAxesVisibility = 0
renderView2.CenterOfRotation = [0.0, -1e-20, 0.0]
renderView2.StereoType = 'Crystal Eyes'
renderView2.CameraPosition = [0.0, 20.636890206955403, 0.0]
renderView2.CameraFocalPoint = [0.0, -1e-20, 0.0]
renderView2.CameraViewUp = [0.0, 0.0, 1.0]
renderView2.CameraFocalDisk = 1.0
renderView2.CameraParallelScale = 7.820080520075376
renderView2.BackEnd = 'OSPRay raycaster'
renderView2.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView3 = CreateView('RenderView')
renderView3.ViewSize = [683, 563]
renderView3.AxesGrid = 'GridAxes3DActor'
renderView3.OrientationAxesVisibility = 0
renderView3.CenterOfRotation = [0.0, -1e-20, 0.0]
renderView3.StereoType = 'Crystal Eyes'
renderView3.CameraPosition = [0.0, 20.636890206955403, 0.0]
renderView3.CameraFocalPoint = [0.0, -1e-20, 0.0]
renderView3.CameraViewUp = [0.0, 0.0, 1.0]
renderView3.CameraFocalDisk = 1.0
renderView3.CameraParallelScale = 7.820080520075376
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
SetActiveView(renderView2)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'XML Image Data Reader'
start_data_omega_bzvti = XMLImageDataReader(registrationName='start_data_omega_bz.vti', FileName=['data/LiH_MICD/vti/start_data_omega_bz.vti'])
start_data_omega_bzvti.CellArrayStatus = ['vtkGhostType']
start_data_omega_bzvti.PointArrayStatus = ['bz_wz', 'omega_bz', 'vtkValidPointMask', 'vtkGhostType']
start_data_omega_bzvti.TimeArray = 'None'

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
threshold1.UpperThreshold = 0.8493308367608376

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother2 = TTKGeometrySmoother(registrationName='TTKGeometrySmoother2', Input=threshold1)
tTKGeometrySmoother2.IterationNumber = 2
tTKGeometrySmoother2.InputMaskField = ['POINTS', 'oppositeOmega']

# create a new 'Contour'
contour1 = Contour(registrationName='Contour1', Input=start_data_omega_bzvti)
contour1.ContourBy = ['POINTS', 'omega_bz']
contour1.Isosurfaces = [0.5]
contour1.PointMergeMethod = 'Uniform Binning'

# create a new 'TTK TopologicalSimplificationByPersistence'
tTKTopologicalSimplificationByPersistence1 = TTKTopologicalSimplificationByPersistence(registrationName='TTKTopologicalSimplificationByPersistence1', Input=start_data_omega_bzvti)
tTKTopologicalSimplificationByPersistence1.InputArray = ['POINTS', 'omega_bz']
tTKTopologicalSimplificationByPersistence1.PersistenceThreshold = 0.5

# create a new 'TTK MorseSmaleComplex'
tTKMorseSmaleComplex1 = TTKMorseSmaleComplex(registrationName='TTKMorseSmaleComplex1', Input=tTKTopologicalSimplificationByPersistence1)
tTKMorseSmaleComplex1.ScalarField = ['POINTS', 'omega_bz']
tTKMorseSmaleComplex1.OffsetField = ['POINTS', 'bz_wz']
tTKMorseSmaleComplex1.AscendingSegmentation = 0
tTKMorseSmaleComplex1.DescendingSegmentation = 0
tTKMorseSmaleComplex1.MorseSmaleComplexSegmentation = 0
tTKMorseSmaleComplex1.ReturnSaddleConnectors = 1
tTKMorseSmaleComplex1.SaddleConnectorsPersistenceThreshold = 0.5

# find source
tTKMorseSmaleComplex1_1 = FindSource('TTKMorseSmaleComplex1')

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother1 = TTKGeometrySmoother(registrationName='TTKGeometrySmoother1', Input=OutputPort(tTKMorseSmaleComplex1_1,1))
tTKGeometrySmoother1.IterationNumber = 1000
tTKGeometrySmoother1.InputMaskField = ['CELLS', 'SeparatrixType']

# create a new 'Threshold'
threshold2 = Threshold(registrationName='Threshold2', Input=tTKGeometrySmoother1)
threshold2.Scalars = ['CELLS', 'SeparatrixType']
threshold2.LowerThreshold = 2.0
threshold2.UpperThreshold = 2.0

# create a new 'Threshold'
threshold3 = Threshold(registrationName='Threshold3', Input=threshold2)
threshold3.Scalars = ['CELLS', 'NumberOfCriticalPointsOnBoundary']
threshold3.LowerThreshold = 1.0
threshold3.UpperThreshold = 1.0

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from contour1
contour1Display = Show(contour1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
contour1Display.Representation = 'Surface'
contour1Display.ColorArrayName = ['POINTS', '']
contour1Display.Opacity = 0.3
contour1Display.Specular = 1.0
contour1Display.SelectTCoordArray = 'None'
contour1Display.SelectNormalArray = 'Normals'
contour1Display.SelectTangentArray = 'None'
contour1Display.OSPRayScaleArray = 'omega_bz'
contour1Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display.SelectOrientationVectors = 'None'
contour1Display.ScaleFactor = 0.846682643890381
contour1Display.SelectScaleArray = 'omega_bz'
contour1Display.GlyphType = 'Arrow'
contour1Display.GlyphTableIndexArray = 'omega_bz'
contour1Display.GaussianRadius = 0.04233413219451904
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
contour1Display.ScaleTransferFunction.Points = [0.6000000238418579, 0.0, 0.5, 0.0, 0.6001220941543579, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour1Display.OpacityTransferFunction.Points = [0.6000000238418579, 0.0, 0.5, 0.0, 0.6001220941543579, 1.0, 0.5, 0.0]

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
tTKMorseSmaleComplex1Display.LineWidth = 10.0
tTKMorseSmaleComplex1Display.RenderLinesAsTubes = 1
tTKMorseSmaleComplex1Display.RenderPointsAsSpheres = 1
tTKMorseSmaleComplex1Display.Specular = 1.0
tTKMorseSmaleComplex1Display.SelectTCoordArray = 'None'
tTKMorseSmaleComplex1Display.SelectNormalArray = 'None'
tTKMorseSmaleComplex1Display.SelectTangentArray = 'None'
tTKMorseSmaleComplex1Display.OSPRayScaleArray = 'CellDimension'
tTKMorseSmaleComplex1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1Display.SelectOrientationVectors = 'None'
tTKMorseSmaleComplex1Display.ScaleFactor = 0.8466827869415283
tTKMorseSmaleComplex1Display.SelectScaleArray = 'CellDimension'
tTKMorseSmaleComplex1Display.GlyphType = 'Arrow'
tTKMorseSmaleComplex1Display.GlyphTableIndexArray = 'CellDimension'
tTKMorseSmaleComplex1Display.GaussianRadius = 0.042334139347076416
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
tTKMorseSmaleComplex1_3Display.ScaleFactor = 1.006182531816462
tTKMorseSmaleComplex1_3Display.SelectScaleArray = 'None'
tTKMorseSmaleComplex1_3Display.GlyphType = 'Arrow'
tTKMorseSmaleComplex1_3Display.GlyphTableIndexArray = 'None'
tTKMorseSmaleComplex1_3Display.GaussianRadius = 0.050309126590823094
tTKMorseSmaleComplex1_3Display.SetScaleArray = ['POINTS', 'bz_wz']
tTKMorseSmaleComplex1_3Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1_3Display.OpacityArray = ['POINTS', 'bz_wz']
tTKMorseSmaleComplex1_3Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1_3Display.DataAxesGrid = 'GridAxesRepresentation'
tTKMorseSmaleComplex1_3Display.PolarAxes = 'PolarAxesRepresentation'
tTKMorseSmaleComplex1_3Display.ScalarOpacityUnitDistance = 0.12315087617612483
tTKMorseSmaleComplex1_3Display.OpacityArrayName = ['POINTS', 'bz_wz']
tTKMorseSmaleComplex1_3Display.SliceFunction = 'Plane'
tTKMorseSmaleComplex1_3Display.Slice = 63
tTKMorseSmaleComplex1_3Display.SelectInputVectors = ['POINTS', 'bz_wz']
tTKMorseSmaleComplex1_3Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKMorseSmaleComplex1_3Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKMorseSmaleComplex1_3Display.ScaleTransferFunction.Points = [-0.7038620845610734, 0.0, 0.5, 0.0, 9.253598515594783, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKMorseSmaleComplex1_3Display.OpacityTransferFunction.Points = [-0.7038620845610734, 0.0, 0.5, 0.0, 9.253598515594783, 1.0, 0.5, 0.0]

# show data from tTKGeometrySmoother1
tTKGeometrySmoother1Display = Show(tTKGeometrySmoother1, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'SeparatrixType'
separatrixTypeLUT = GetColorTransferFunction('SeparatrixType')
separatrixTypeLUT.RGBPoints = [0.0, 0.0, 0.129412, 0.584314, 1.0002441406250009, 0.917647, 0.941176, 0.788235, 2.00048828125, 0.0, 0.431373, 0.0]
separatrixTypeLUT.ColorSpace = 'RGB'
separatrixTypeLUT.AboveRangeColor = [1.0, 1.0, 1.0]
separatrixTypeLUT.NanColor = [0.0, 0.0, 0.0]
separatrixTypeLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
tTKGeometrySmoother1Display.Representation = 'Surface'
tTKGeometrySmoother1Display.ColorArrayName = ['CELLS', 'SeparatrixType']
tTKGeometrySmoother1Display.LookupTable = separatrixTypeLUT
tTKGeometrySmoother1Display.LineWidth = 5.0
tTKGeometrySmoother1Display.RenderLinesAsTubes = 1
tTKGeometrySmoother1Display.Specular = 1.0
tTKGeometrySmoother1Display.SelectTCoordArray = 'None'
tTKGeometrySmoother1Display.SelectNormalArray = 'None'
tTKGeometrySmoother1Display.SelectTangentArray = 'None'
tTKGeometrySmoother1Display.OSPRayScaleArray = 'CellDimension'
tTKGeometrySmoother1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKGeometrySmoother1Display.SelectOrientationVectors = 'None'
tTKGeometrySmoother1Display.ScaleFactor = 0.9348782539367676
tTKGeometrySmoother1Display.SelectScaleArray = 'SeparatrixType'
tTKGeometrySmoother1Display.GlyphType = 'Arrow'
tTKGeometrySmoother1Display.GlyphTableIndexArray = 'SeparatrixType'
tTKGeometrySmoother1Display.GaussianRadius = 0.04674391269683838
tTKGeometrySmoother1Display.SetScaleArray = ['POINTS', 'CellDimension']
tTKGeometrySmoother1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKGeometrySmoother1Display.OpacityArray = ['POINTS', 'CellDimension']
tTKGeometrySmoother1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKGeometrySmoother1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKGeometrySmoother1Display.PolarAxes = 'PolarAxesRepresentation'
tTKGeometrySmoother1Display.SelectInputVectors = ['POINTS', 'CellDimension']
tTKGeometrySmoother1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKGeometrySmoother1Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKGeometrySmoother1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKGeometrySmoother1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

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
start_data_omega_bzvtiDisplay.ScaleFactor = 1.006182531816462
start_data_omega_bzvtiDisplay.SelectScaleArray = 'None'
start_data_omega_bzvtiDisplay.GlyphType = 'Arrow'
start_data_omega_bzvtiDisplay.GlyphTableIndexArray = 'None'
start_data_omega_bzvtiDisplay.GaussianRadius = 0.050309126590823094
start_data_omega_bzvtiDisplay.SetScaleArray = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay.ScaleTransferFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay.OpacityArray = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay.OpacityTransferFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay.DataAxesGrid = 'GridAxesRepresentation'
start_data_omega_bzvtiDisplay.PolarAxes = 'PolarAxesRepresentation'
start_data_omega_bzvtiDisplay.ScalarOpacityUnitDistance = 0.12315087617612483
start_data_omega_bzvtiDisplay.OpacityArrayName = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay.SliceFunction = 'Plane'
start_data_omega_bzvtiDisplay.Slice = 63
start_data_omega_bzvtiDisplay.SelectInputVectors = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
start_data_omega_bzvtiDisplay.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
start_data_omega_bzvtiDisplay.ScaleTransferFunction.Points = [-0.7038620845610734, 0.0, 0.5, 0.0, 9.253598515594783, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
start_data_omega_bzvtiDisplay.OpacityTransferFunction.Points = [-0.7038620845610734, 0.0, 0.5, 0.0, 9.253598515594783, 1.0, 0.5, 0.0]

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
contour1Display_1.ScaleFactor = 0.8636709690093994
contour1Display_1.SelectScaleArray = 'omega_bz'
contour1Display_1.GlyphType = 'Arrow'
contour1Display_1.GlyphTableIndexArray = 'omega_bz'
contour1Display_1.GaussianRadius = 0.04318354845046997
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

# show data from tTKGeometrySmoother2
tTKGeometrySmoother2Display = Show(tTKGeometrySmoother2, renderView2, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'Persistence'
persistenceLUT = GetColorTransferFunction('Persistence')
persistenceLUT.RGBPoints = [7.237523249419703e-06, 0.0, 0.129412, 0.584314, 0.42473007516535743, 0.917647, 0.941176, 0.788235, 0.8494529128074646, 0.0, 0.431373, 0.0]
persistenceLUT.ColorSpace = 'RGB'
persistenceLUT.AboveRangeColor = [1.0, 1.0, 1.0]
persistenceLUT.NanColor = [0.0, 0.0, 0.0]
persistenceLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'Persistence'
persistencePWF = GetOpacityTransferFunction('Persistence')
persistencePWF.Points = [7.237523249419703e-06, 0.0, 0.5, 0.0, 0.8494529128074646, 1.0, 0.5, 0.0]
persistencePWF.ScalarRangeInitialized = 1

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
tTKGeometrySmoother2Display.OSPRayScaleArray = 'oppositeOmega'
tTKGeometrySmoother2Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKGeometrySmoother2Display.SelectOrientationVectors = 'None'
tTKGeometrySmoother2Display.ScaleFactor = 0.07141872048377991
tTKGeometrySmoother2Display.SelectScaleArray = 'None'
tTKGeometrySmoother2Display.GlyphType = 'Arrow'
tTKGeometrySmoother2Display.GlyphTableIndexArray = 'None'
tTKGeometrySmoother2Display.GaussianRadius = 0.0035709360241889952
tTKGeometrySmoother2Display.SetScaleArray = ['POINTS', 'oppositeOmega']
tTKGeometrySmoother2Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKGeometrySmoother2Display.OpacityArray = ['POINTS', 'oppositeOmega']
tTKGeometrySmoother2Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKGeometrySmoother2Display.DataAxesGrid = 'GridAxesRepresentation'
tTKGeometrySmoother2Display.PolarAxes = 'PolarAxesRepresentation'
tTKGeometrySmoother2Display.ScalarOpacityFunction = persistencePWF
tTKGeometrySmoother2Display.ScalarOpacityUnitDistance = 0.21744076418518754
tTKGeometrySmoother2Display.OpacityArrayName = ['POINTS', 'oppositeOmega']
tTKGeometrySmoother2Display.SelectInputVectors = ['POINTS', 'oppositeOmega']
tTKGeometrySmoother2Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKGeometrySmoother2Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKGeometrySmoother2Display.ScaleTransferFunction.Points = [-0.9751526647579255, 0.0, 0.5, 0.0, -0.9056711359213363, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKGeometrySmoother2Display.OpacityTransferFunction.Points = [-0.9751526647579255, 0.0, 0.5, 0.0, -0.9056711359213363, 1.0, 0.5, 0.0]

# ----------------------------------------------------------------
# setup the visualization in view 'renderView3'
# ----------------------------------------------------------------

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
start_data_omega_bzvtiDisplay_1.ScaleFactor = 1.006182531816462
start_data_omega_bzvtiDisplay_1.SelectScaleArray = 'None'
start_data_omega_bzvtiDisplay_1.GlyphType = 'Arrow'
start_data_omega_bzvtiDisplay_1.GlyphTableIndexArray = 'None'
start_data_omega_bzvtiDisplay_1.GaussianRadius = 0.050309126590823094
start_data_omega_bzvtiDisplay_1.SetScaleArray = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_1.ScaleTransferFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay_1.OpacityArray = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_1.OpacityTransferFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay_1.DataAxesGrid = 'GridAxesRepresentation'
start_data_omega_bzvtiDisplay_1.PolarAxes = 'PolarAxesRepresentation'
start_data_omega_bzvtiDisplay_1.ScalarOpacityUnitDistance = 0.12315087617612483
start_data_omega_bzvtiDisplay_1.OpacityArrayName = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_1.SliceFunction = 'Plane'
start_data_omega_bzvtiDisplay_1.Slice = 63
start_data_omega_bzvtiDisplay_1.SelectInputVectors = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_1.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
start_data_omega_bzvtiDisplay_1.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
start_data_omega_bzvtiDisplay_1.ScaleTransferFunction.Points = [-0.7038620845610734, 0.0, 0.5, 0.0, 9.253598515594783, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
start_data_omega_bzvtiDisplay_1.OpacityTransferFunction.Points = [-0.7038620845610734, 0.0, 0.5, 0.0, 9.253598515594783, 1.0, 0.5, 0.0]

# show data from contour1
contour1Display_2 = Show(contour1, renderView3, 'GeometryRepresentation')

# trace defaults for the display properties.
contour1Display_2.Representation = 'Surface'
contour1Display_2.ColorArrayName = ['POINTS', '']
contour1Display_2.Opacity = 0.1
contour1Display_2.Specular = 1.0
contour1Display_2.SelectTCoordArray = 'None'
contour1Display_2.SelectNormalArray = 'Normals'
contour1Display_2.SelectTangentArray = 'None'
contour1Display_2.OSPRayScaleArray = 'omega_bz'
contour1Display_2.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display_2.SelectOrientationVectors = 'None'
contour1Display_2.ScaleFactor = 0.8636709690093994
contour1Display_2.SelectScaleArray = 'omega_bz'
contour1Display_2.GlyphType = 'Arrow'
contour1Display_2.GlyphTableIndexArray = 'omega_bz'
contour1Display_2.GaussianRadius = 0.04318354845046997
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

# show data from threshold3
threshold3Display = Show(threshold3, renderView3, 'UnstructuredGridRepresentation')

# get opacity transfer function/opacity map for 'SeparatrixType'
separatrixTypePWF = GetOpacityTransferFunction('SeparatrixType')
separatrixTypePWF.Points = [0.0, 0.0, 0.5, 0.0, 2.00048828125, 1.0, 0.5, 0.0]
separatrixTypePWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
threshold3Display.Representation = 'Surface'
threshold3Display.ColorArrayName = ['CELLS', 'SeparatrixType']
threshold3Display.LookupTable = separatrixTypeLUT
threshold3Display.LineWidth = 10.0
threshold3Display.RenderLinesAsTubes = 1
threshold3Display.Specular = 1.0
threshold3Display.SelectTCoordArray = 'None'
threshold3Display.SelectNormalArray = 'None'
threshold3Display.SelectTangentArray = 'None'
threshold3Display.OSPRayScaleArray = 'CellDimension'
threshold3Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold3Display.SelectOrientationVectors = 'None'
threshold3Display.ScaleFactor = 0.8466827869415283
threshold3Display.SelectScaleArray = 'SeparatrixType'
threshold3Display.GlyphType = 'Arrow'
threshold3Display.GlyphTableIndexArray = 'SeparatrixType'
threshold3Display.GaussianRadius = 0.042334139347076416
threshold3Display.SetScaleArray = ['POINTS', 'CellDimension']
threshold3Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold3Display.OpacityArray = ['POINTS', 'CellDimension']
threshold3Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold3Display.DataAxesGrid = 'GridAxesRepresentation'
threshold3Display.PolarAxes = 'PolarAxesRepresentation'
threshold3Display.ScalarOpacityFunction = separatrixTypePWF
threshold3Display.ScalarOpacityUnitDistance = 0.9099565514149196
threshold3Display.OpacityArrayName = ['CELLS', 'SeparatrixType']
threshold3Display.SelectInputVectors = ['POINTS', 'CellDimension']
threshold3Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
threshold3Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold3Display.ScaleTransferFunction.Points = [2.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold3Display.OpacityTransferFunction.Points = [2.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

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
SetActiveSource(threshold3)
# ----------------------------------------------------------------


if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')
