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
renderView1.CameraPosition = [30.816017241199855, -2.9411717603847247, 9.864173922480386]
renderView1.CameraFocalPoint = [0.37892830661347293, -0.08239876250381083, -1.075784185744124]
renderView1.CameraViewUp = [-0.3313637586266201, 0.07205575084496531, 0.9407475900787668]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 10.168522755667778
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView2 = CreateView('RenderView')
renderView2.ViewSize = [684, 563]
renderView2.AxesGrid = 'GridAxes3DActor'
renderView2.OrientationAxesVisibility = 0
renderView2.StereoType = 'Crystal Eyes'
renderView2.CameraPosition = [30.816017241199855, -2.9411717603847247, 9.864173922480386]
renderView2.CameraFocalPoint = [0.37892830661347293, -0.08239876250381083, -1.075784185744124]
renderView2.CameraViewUp = [-0.3313637586266201, 0.07205575084496531, 0.9407475900787668]
renderView2.CameraFocalDisk = 1.0
renderView2.CameraParallelScale = 10.168522755667778
renderView2.BackEnd = 'OSPRay raycaster'
renderView2.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView3 = CreateView('RenderView')
renderView3.ViewSize = [683, 563]
renderView3.AxesGrid = 'GridAxes3DActor'
renderView3.OrientationAxesVisibility = 0
renderView3.StereoType = 'Crystal Eyes'
renderView3.CameraPosition = [30.816017241199855, -2.9411717603847247, 9.864173922480386]
renderView3.CameraFocalPoint = [0.37892830661347293, -0.08239876250381083, -1.075784185744124]
renderView3.CameraViewUp = [-0.3313637586266201, 0.07205575084496531, 0.9407475900787668]
renderView3.CameraFocalDisk = 1.0
renderView3.CameraParallelScale = 10.168522755667778
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
start_data_omega_bzvti = XMLImageDataReader(registrationName='start_data_omega_bz.vti', FileName=['data/C6H6_MICD/vti/start_data_omega_bz.vti'])
start_data_omega_bzvti.CellArrayStatus = ['vtkGhostType']
start_data_omega_bzvti.PointArrayStatus = ['bz_wz', 'omega_bz', 'vtkValidPointMask', 'vtkGhostType']
start_data_omega_bzvti.TimeArray = 'None'

# create a new 'TTK TopologicalSimplificationByPersistence'
tTKTopologicalSimplificationByPersistence1 = TTKTopologicalSimplificationByPersistence(registrationName='TTKTopologicalSimplificationByPersistence1', Input=start_data_omega_bzvti)
tTKTopologicalSimplificationByPersistence1.InputArray = ['POINTS', 'omega_bz']
tTKTopologicalSimplificationByPersistence1.PersistenceThreshold = 0.4

# create a new 'TTK MorseSmaleComplex'
tTKMorseSmaleComplex1 = TTKMorseSmaleComplex(registrationName='TTKMorseSmaleComplex1', Input=tTKTopologicalSimplificationByPersistence1)
tTKMorseSmaleComplex1.ScalarField = ['POINTS', 'omega_bz']
tTKMorseSmaleComplex1.OffsetField = ['POINTS', 'bz_wz']
tTKMorseSmaleComplex1.AscendingSegmentation = 0
tTKMorseSmaleComplex1.DescendingSegmentation = 0
tTKMorseSmaleComplex1.MorseSmaleComplexSegmentation = 0
tTKMorseSmaleComplex1.SaddleConnectorsPersistenceThreshold = 0.4

# find source
tTKMorseSmaleComplex1_1 = FindSource('TTKMorseSmaleComplex1')

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother3 = TTKGeometrySmoother(registrationName='TTKGeometrySmoother3', Input=OutputPort(tTKMorseSmaleComplex1_1,1))
tTKGeometrySmoother3.IterationNumber = 100
tTKGeometrySmoother3.InputMaskField = ['CELLS', 'SeparatrixType']

# create a new 'TTK PersistentGenerators'
tTKPersistentGenerators1 = TTKPersistentGenerators(registrationName='TTKPersistentGenerators1', Input=start_data_omega_bzvti)
tTKPersistentGenerators1.ScalarField = ['POINTS', 'omega_bz']
tTKPersistentGenerators1.InputOffsetField = ['POINTS', 'bz_wz']

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=start_data_omega_bzvti)
calculator1.ResultArrayName = 'oppositeOmega'
calculator1.Function = '-omega_bz'

# create a new 'TTK PersistentGenerators'
tTKPersistentGenerators2 = TTKPersistentGenerators(registrationName='TTKPersistentGenerators2', Input=calculator1)
tTKPersistentGenerators2.ScalarField = ['POINTS', 'oppositeOmega']
tTKPersistentGenerators2.InputOffsetField = ['POINTS', 'oppositeOmega']

# create a new 'Threshold'
threshold3 = Threshold(registrationName='Threshold3', Input=tTKPersistentGenerators2)
threshold3.Scalars = ['CELLS', 'ComponentId']

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother2 = TTKGeometrySmoother(registrationName='TTKGeometrySmoother2', Input=threshold3)
tTKGeometrySmoother2.IterationNumber = 10
tTKGeometrySmoother2.InputMaskField = ['POINTS', '']

# create a new 'Threshold'
threshold4 = Threshold(registrationName='Threshold4', Input=tTKGeometrySmoother2)
threshold4.Scalars = ['CELLS', 'Persistence']
threshold4.LowerThreshold = 0.5
threshold4.UpperThreshold = 0.5915350587181316

# create a new 'Threshold'
threshold1 = Threshold(registrationName='Threshold1', Input=tTKPersistentGenerators1)
threshold1.Scalars = ['CELLS', 'ComponentId']

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother1 = TTKGeometrySmoother(registrationName='TTKGeometrySmoother1', Input=threshold1)
tTKGeometrySmoother1.IterationNumber = 10
tTKGeometrySmoother1.InputMaskField = ['POINTS', '']

# create a new 'Threshold'
threshold2 = Threshold(registrationName='Threshold2', Input=tTKGeometrySmoother1)
threshold2.Scalars = ['CELLS', 'Persistence']
threshold2.LowerThreshold = 0.6
threshold2.UpperThreshold = 0.6502380218673928

# create a new 'Contour'
contour1 = Contour(registrationName='Contour1', Input=start_data_omega_bzvti)
contour1.ContourBy = ['POINTS', 'omega_bz']
contour1.Isosurfaces = [0.5]
contour1.PointMergeMethod = 'Uniform Binning'

# create a new 'Threshold'
threshold5 = Threshold(registrationName='Threshold5', Input=tTKGeometrySmoother3)
threshold5.Scalars = ['CELLS', 'SeparatrixType']
threshold5.LowerThreshold = 2.0
threshold5.UpperThreshold = 2.0

# create a new 'Threshold'
threshold6 = Threshold(registrationName='Threshold6', Input=threshold5)
threshold6.Scalars = ['CELLS', 'NumberOfCriticalPointsOnBoundary']
threshold6.LowerThreshold = 1.0
threshold6.UpperThreshold = 1.0

# create a new 'Threshold'
threshold7 = Threshold(registrationName='Threshold7', Input=threshold6)
threshold7.Scalars = ['CELLS', 'SeparatrixFunctionMinimum']
threshold7.LowerThreshold = 0.4
threshold7.UpperThreshold = 0.855108512790093

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from contour1
contour1Display = Show(contour1, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'omega_bz'
omega_bzLUT = GetColorTransferFunction('omega_bz')
omega_bzLUT.RGBPoints = [0.5, 0.0, 0.129412, 0.584314, 0.50006103515625, 0.917647, 0.941176, 0.788235, 0.5001220703125, 0.0, 0.431373, 0.0]
omega_bzLUT.ColorSpace = 'RGB'
omega_bzLUT.AboveRangeColor = [1.0, 1.0, 1.0]
omega_bzLUT.NanColor = [0.0, 0.0, 0.0]
omega_bzLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
contour1Display.Representation = 'Surface'
contour1Display.ColorArrayName = ['POINTS', '']
contour1Display.LookupTable = omega_bzLUT
contour1Display.Opacity = 0.1
contour1Display.Specular = 1.0
contour1Display.SelectTCoordArray = 'None'
contour1Display.SelectNormalArray = 'Normals'
contour1Display.SelectTangentArray = 'None'
contour1Display.OSPRayScaleArray = 'omega_bz'
contour1Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display.SelectOrientationVectors = 'None'
contour1Display.ScaleFactor = 1.340131187438965
contour1Display.SelectScaleArray = 'omega_bz'
contour1Display.GlyphType = 'Arrow'
contour1Display.GlyphTableIndexArray = 'omega_bz'
contour1Display.GaussianRadius = 0.06700655937194824
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
tTKMorseSmaleComplex1Display.PointSize = 15.0
tTKMorseSmaleComplex1Display.RenderPointsAsSpheres = 1
tTKMorseSmaleComplex1Display.Specular = 1.0
tTKMorseSmaleComplex1Display.SelectTCoordArray = 'None'
tTKMorseSmaleComplex1Display.SelectNormalArray = 'None'
tTKMorseSmaleComplex1Display.SelectTangentArray = 'None'
tTKMorseSmaleComplex1Display.OSPRayScaleArray = 'CellDimension'
tTKMorseSmaleComplex1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1Display.SelectOrientationVectors = 'None'
tTKMorseSmaleComplex1Display.ScaleFactor = 1.3401312828063965
tTKMorseSmaleComplex1Display.SelectScaleArray = 'CellDimension'
tTKMorseSmaleComplex1Display.GlyphType = 'Arrow'
tTKMorseSmaleComplex1Display.GlyphTableIndexArray = 'CellDimension'
tTKMorseSmaleComplex1Display.GaussianRadius = 0.06700656414031983
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
tTKMorseSmaleComplex1_2Display.ColorArrayName = ['POINTS', '']
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
tTKMorseSmaleComplex1_2Display.SetScaleArray = ['POINTS', '']
tTKMorseSmaleComplex1_2Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1_2Display.OpacityArray = ['POINTS', '']
tTKMorseSmaleComplex1_2Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1_2Display.DataAxesGrid = 'GridAxesRepresentation'
tTKMorseSmaleComplex1_2Display.PolarAxes = 'PolarAxesRepresentation'
tTKMorseSmaleComplex1_2Display.SelectInputVectors = ['POINTS', '']
tTKMorseSmaleComplex1_2Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKMorseSmaleComplex1_2Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# find source
tTKMorseSmaleComplex1_3 = FindSource('TTKMorseSmaleComplex1')

# show data from tTKMorseSmaleComplex1_3
tTKMorseSmaleComplex1_3Display = Show(OutputPort(tTKMorseSmaleComplex1_3, 3), renderView1, 'UniformGridRepresentation')

# trace defaults for the display properties.
tTKMorseSmaleComplex1_3Display.Representation = 'Outline'
tTKMorseSmaleComplex1_3Display.ColorArrayName = ['POINTS', '']
tTKMorseSmaleComplex1_3Display.SelectTCoordArray = 'None'
tTKMorseSmaleComplex1_3Display.SelectNormalArray = 'None'
tTKMorseSmaleComplex1_3Display.SelectTangentArray = 'None'
tTKMorseSmaleComplex1_3Display.OSPRayScaleArray = 'bz_wz'
tTKMorseSmaleComplex1_3Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1_3Display.SelectOrientationVectors = 'None'
tTKMorseSmaleComplex1_3Display.ScaleFactor = 1.340131197867462
tTKMorseSmaleComplex1_3Display.SelectScaleArray = 'None'
tTKMorseSmaleComplex1_3Display.GlyphType = 'Arrow'
tTKMorseSmaleComplex1_3Display.GlyphTableIndexArray = 'None'
tTKMorseSmaleComplex1_3Display.GaussianRadius = 0.06700655989337309
tTKMorseSmaleComplex1_3Display.SetScaleArray = ['POINTS', 'bz_wz']
tTKMorseSmaleComplex1_3Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1_3Display.OpacityArray = ['POINTS', 'bz_wz']
tTKMorseSmaleComplex1_3Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1_3Display.DataAxesGrid = 'GridAxesRepresentation'
tTKMorseSmaleComplex1_3Display.PolarAxes = 'PolarAxesRepresentation'
tTKMorseSmaleComplex1_3Display.ScalarOpacityUnitDistance = 0.16013421963098115
tTKMorseSmaleComplex1_3Display.OpacityArrayName = ['POINTS', 'bz_wz']
tTKMorseSmaleComplex1_3Display.SliceFunction = 'Plane'
tTKMorseSmaleComplex1_3Display.Slice = 63
tTKMorseSmaleComplex1_3Display.SelectInputVectors = ['POINTS', 'bz_wz']
tTKMorseSmaleComplex1_3Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKMorseSmaleComplex1_3Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKMorseSmaleComplex1_3Display.ScaleTransferFunction.Points = [-4.465061260008894, 0.0, 0.5, 0.0, 71.75408448849733, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKMorseSmaleComplex1_3Display.OpacityTransferFunction.Points = [-4.465061260008894, 0.0, 0.5, 0.0, 71.75408448849733, 1.0, 0.5, 0.0]

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
tTKGeometrySmoother3Display.Specular = 1.0
tTKGeometrySmoother3Display.SelectTCoordArray = 'None'
tTKGeometrySmoother3Display.SelectNormalArray = 'None'
tTKGeometrySmoother3Display.SelectTangentArray = 'None'
tTKGeometrySmoother3Display.OSPRayScaleArray = 'CellDimension'
tTKGeometrySmoother3Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKGeometrySmoother3Display.SelectOrientationVectors = 'None'
tTKGeometrySmoother3Display.ScaleFactor = 1.3401310920715332
tTKGeometrySmoother3Display.SelectScaleArray = 'SeparatrixType'
tTKGeometrySmoother3Display.GlyphType = 'Arrow'
tTKGeometrySmoother3Display.GlyphTableIndexArray = 'SeparatrixType'
tTKGeometrySmoother3Display.GaussianRadius = 0.06700655460357666
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
start_data_omega_bzvtiDisplay.ColorArrayName = ['POINTS', '']
start_data_omega_bzvtiDisplay.SelectTCoordArray = 'None'
start_data_omega_bzvtiDisplay.SelectNormalArray = 'None'
start_data_omega_bzvtiDisplay.SelectTangentArray = 'None'
start_data_omega_bzvtiDisplay.OSPRayScaleArray = 'bz_wz'
start_data_omega_bzvtiDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay.SelectOrientationVectors = 'None'
start_data_omega_bzvtiDisplay.ScaleFactor = 1.340131197867462
start_data_omega_bzvtiDisplay.SelectScaleArray = 'None'
start_data_omega_bzvtiDisplay.GlyphType = 'Arrow'
start_data_omega_bzvtiDisplay.GlyphTableIndexArray = 'None'
start_data_omega_bzvtiDisplay.GaussianRadius = 0.06700655989337309
start_data_omega_bzvtiDisplay.SetScaleArray = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay.ScaleTransferFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay.OpacityArray = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay.OpacityTransferFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay.DataAxesGrid = 'GridAxesRepresentation'
start_data_omega_bzvtiDisplay.PolarAxes = 'PolarAxesRepresentation'
start_data_omega_bzvtiDisplay.ScalarOpacityUnitDistance = 0.16013421963098115
start_data_omega_bzvtiDisplay.OpacityArrayName = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay.SliceFunction = 'Plane'
start_data_omega_bzvtiDisplay.Slice = 63
start_data_omega_bzvtiDisplay.SelectInputVectors = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
start_data_omega_bzvtiDisplay.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
start_data_omega_bzvtiDisplay.ScaleTransferFunction.Points = [-4.465061260008894, 0.0, 0.5, 0.0, 71.75408448849733, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
start_data_omega_bzvtiDisplay.OpacityTransferFunction.Points = [-4.465061260008894, 0.0, 0.5, 0.0, 71.75408448849733, 1.0, 0.5, 0.0]

# show data from contour1
contour1Display_1 = Show(contour1, renderView2, 'GeometryRepresentation')

# trace defaults for the display properties.
contour1Display_1.Representation = 'Surface'
contour1Display_1.ColorArrayName = ['POINTS', '']
contour1Display_1.LookupTable = omega_bzLUT
contour1Display_1.Opacity = 0.1
contour1Display_1.Specular = 1.0
contour1Display_1.SelectTCoordArray = 'None'
contour1Display_1.SelectNormalArray = 'Normals'
contour1Display_1.SelectTangentArray = 'None'
contour1Display_1.OSPRayScaleArray = 'omega_bz'
contour1Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display_1.SelectOrientationVectors = 'None'
contour1Display_1.ScaleFactor = 1.340131187438965
contour1Display_1.SelectScaleArray = 'omega_bz'
contour1Display_1.GlyphType = 'Arrow'
contour1Display_1.GlyphTableIndexArray = 'omega_bz'
contour1Display_1.GaussianRadius = 0.06700655937194824
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

# show data from threshold2
threshold2Display = Show(threshold2, renderView2, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'Persistence'
persistenceLUT = GetColorTransferFunction('Persistence')
persistenceLUT.RGBPoints = [0.5256653228388577, 0.0, 0.129412, 0.584314, 0.5879516723531253, 0.917647, 0.941176, 0.788235, 0.6502380218673928, 0.0, 0.431373, 0.0]
persistenceLUT.ColorSpace = 'RGB'
persistenceLUT.AboveRangeColor = [1.0, 1.0, 1.0]
persistenceLUT.NanColor = [0.0, 0.0, 0.0]
persistenceLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'Persistence'
persistencePWF = GetOpacityTransferFunction('Persistence')
persistencePWF.Points = [0.5256653228388577, 0.0, 0.5, 0.0, 0.6502380218673928, 1.0, 0.5, 0.0]
persistencePWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
threshold2Display.Representation = 'Surface'
threshold2Display.ColorArrayName = ['CELLS', 'Persistence']
threshold2Display.LookupTable = persistenceLUT
threshold2Display.LineWidth = 10.0
threshold2Display.RenderLinesAsTubes = 1
threshold2Display.Specular = 1.0
threshold2Display.SelectTCoordArray = 'None'
threshold2Display.SelectNormalArray = 'None'
threshold2Display.SelectTangentArray = 'None'
threshold2Display.OSPRayScaleArray = 'omega_bz'
threshold2Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold2Display.SelectOrientationVectors = 'None'
threshold2Display.ScaleFactor = 1.3401310920715332
threshold2Display.SelectScaleArray = 'None'
threshold2Display.GlyphType = 'Arrow'
threshold2Display.GlyphTableIndexArray = 'None'
threshold2Display.GaussianRadius = 0.06700655460357666
threshold2Display.SetScaleArray = ['POINTS', 'omega_bz']
threshold2Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold2Display.OpacityArray = ['POINTS', 'omega_bz']
threshold2Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold2Display.DataAxesGrid = 'GridAxesRepresentation'
threshold2Display.PolarAxes = 'PolarAxesRepresentation'
threshold2Display.ScalarOpacityFunction = persistencePWF
threshold2Display.ScalarOpacityUnitDistance = 1.25486282689788
threshold2Display.OpacityArrayName = ['POINTS', 'omega_bz']
threshold2Display.SelectInputVectors = ['POINTS', 'omega_bz']
threshold2Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
threshold2Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold2Display.ScaleTransferFunction.Points = [0.0027159030315205587, 0.0, 0.5, 0.0, 0.21960135494369434, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold2Display.OpacityTransferFunction.Points = [0.0027159030315205587, 0.0, 0.5, 0.0, 0.21960135494369434, 1.0, 0.5, 0.0]

# show data from threshold4
threshold4Display = Show(threshold4, renderView2, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
threshold4Display.Representation = 'Surface'
threshold4Display.ColorArrayName = ['CELLS', 'Persistence']
threshold4Display.LookupTable = persistenceLUT
threshold4Display.LineWidth = 10.0
threshold4Display.RenderLinesAsTubes = 1
threshold4Display.Specular = 1.0
threshold4Display.SelectTCoordArray = 'None'
threshold4Display.SelectNormalArray = 'None'
threshold4Display.SelectTangentArray = 'None'
threshold4Display.OSPRayScaleArray = 'oppositeOmega'
threshold4Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold4Display.SelectOrientationVectors = 'None'
threshold4Display.ScaleFactor = 0.578649377822876
threshold4Display.SelectScaleArray = 'None'
threshold4Display.GlyphType = 'Arrow'
threshold4Display.GlyphTableIndexArray = 'None'
threshold4Display.GaussianRadius = 0.0289324688911438
threshold4Display.SetScaleArray = ['POINTS', 'oppositeOmega']
threshold4Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold4Display.OpacityArray = ['POINTS', 'oppositeOmega']
threshold4Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold4Display.DataAxesGrid = 'GridAxesRepresentation'
threshold4Display.PolarAxes = 'PolarAxesRepresentation'
threshold4Display.ScalarOpacityFunction = persistencePWF
threshold4Display.ScalarOpacityUnitDistance = 0.8531844661377084
threshold4Display.OpacityArrayName = ['POINTS', 'oppositeOmega']
threshold4Display.SelectInputVectors = ['POINTS', 'oppositeOmega']
threshold4Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
threshold4Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold4Display.ScaleTransferFunction.Points = [-0.989022796926287, 0.0, 0.5, 0.0, -0.7283422585957536, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold4Display.OpacityTransferFunction.Points = [-0.989022796926287, 0.0, 0.5, 0.0, -0.7283422585957536, 1.0, 0.5, 0.0]

# ----------------------------------------------------------------
# setup the visualization in view 'renderView3'
# ----------------------------------------------------------------

# show data from contour1
contour1Display_2 = Show(contour1, renderView3, 'GeometryRepresentation')

# trace defaults for the display properties.
contour1Display_2.Representation = 'Surface'
contour1Display_2.ColorArrayName = ['POINTS', '']
contour1Display_2.LookupTable = omega_bzLUT
contour1Display_2.Opacity = 0.1
contour1Display_2.Specular = 1.0
contour1Display_2.SelectTCoordArray = 'None'
contour1Display_2.SelectNormalArray = 'Normals'
contour1Display_2.SelectTangentArray = 'None'
contour1Display_2.OSPRayScaleArray = 'omega_bz'
contour1Display_2.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display_2.SelectOrientationVectors = 'None'
contour1Display_2.ScaleFactor = 1.340131187438965
contour1Display_2.SelectScaleArray = 'omega_bz'
contour1Display_2.GlyphType = 'Arrow'
contour1Display_2.GlyphTableIndexArray = 'omega_bz'
contour1Display_2.GaussianRadius = 0.06700655937194824
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
start_data_omega_bzvtiDisplay_1.ColorArrayName = ['POINTS', '']
start_data_omega_bzvtiDisplay_1.SelectTCoordArray = 'None'
start_data_omega_bzvtiDisplay_1.SelectNormalArray = 'None'
start_data_omega_bzvtiDisplay_1.SelectTangentArray = 'None'
start_data_omega_bzvtiDisplay_1.OSPRayScaleArray = 'bz_wz'
start_data_omega_bzvtiDisplay_1.OSPRayScaleFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay_1.SelectOrientationVectors = 'None'
start_data_omega_bzvtiDisplay_1.ScaleFactor = 1.340131197867462
start_data_omega_bzvtiDisplay_1.SelectScaleArray = 'None'
start_data_omega_bzvtiDisplay_1.GlyphType = 'Arrow'
start_data_omega_bzvtiDisplay_1.GlyphTableIndexArray = 'None'
start_data_omega_bzvtiDisplay_1.GaussianRadius = 0.06700655989337309
start_data_omega_bzvtiDisplay_1.SetScaleArray = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_1.ScaleTransferFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay_1.OpacityArray = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_1.OpacityTransferFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay_1.DataAxesGrid = 'GridAxesRepresentation'
start_data_omega_bzvtiDisplay_1.PolarAxes = 'PolarAxesRepresentation'
start_data_omega_bzvtiDisplay_1.ScalarOpacityUnitDistance = 0.16013421963098115
start_data_omega_bzvtiDisplay_1.OpacityArrayName = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_1.SliceFunction = 'Plane'
start_data_omega_bzvtiDisplay_1.Slice = 63
start_data_omega_bzvtiDisplay_1.SelectInputVectors = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_1.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
start_data_omega_bzvtiDisplay_1.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
start_data_omega_bzvtiDisplay_1.ScaleTransferFunction.Points = [-4.465061260008894, 0.0, 0.5, 0.0, 71.75408448849733, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
start_data_omega_bzvtiDisplay_1.OpacityTransferFunction.Points = [-4.465061260008894, 0.0, 0.5, 0.0, 71.75408448849733, 1.0, 0.5, 0.0]

# show data from threshold7
threshold7Display = Show(threshold7, renderView3, 'UnstructuredGridRepresentation')

# get opacity transfer function/opacity map for 'SeparatrixType'
separatrixTypePWF = GetOpacityTransferFunction('SeparatrixType')
separatrixTypePWF.Points = [0.0, 0.0, 0.5, 0.0, 2.00048828125, 1.0, 0.5, 0.0]
separatrixTypePWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
threshold7Display.Representation = 'Surface'
threshold7Display.ColorArrayName = ['CELLS', 'SeparatrixType']
threshold7Display.LookupTable = separatrixTypeLUT
threshold7Display.LineWidth = 10.0
threshold7Display.RenderLinesAsTubes = 1
threshold7Display.Specular = 1.0
threshold7Display.SelectTCoordArray = 'None'
threshold7Display.SelectNormalArray = 'None'
threshold7Display.SelectTangentArray = 'None'
threshold7Display.OSPRayScaleArray = 'CellDimension'
threshold7Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold7Display.SelectOrientationVectors = 'None'
threshold7Display.ScaleFactor = 1.3401312351226808
threshold7Display.SelectScaleArray = 'SeparatrixType'
threshold7Display.GlyphType = 'Arrow'
threshold7Display.GlyphTableIndexArray = 'SeparatrixType'
threshold7Display.GaussianRadius = 0.06700656175613404
threshold7Display.SetScaleArray = ['POINTS', 'CellDimension']
threshold7Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold7Display.OpacityArray = ['POINTS', 'CellDimension']
threshold7Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold7Display.DataAxesGrid = 'GridAxesRepresentation'
threshold7Display.PolarAxes = 'PolarAxesRepresentation'
threshold7Display.ScalarOpacityFunction = separatrixTypePWF
threshold7Display.ScalarOpacityUnitDistance = 1.062225608112421
threshold7Display.OpacityArrayName = ['CELLS', 'SeparatrixType']
threshold7Display.SelectInputVectors = ['POINTS', 'CellDimension']
threshold7Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
threshold7Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold7Display.ScaleTransferFunction.Points = [2.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold7Display.OpacityTransferFunction.Points = [2.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'omega_bz'
omega_bzPWF = GetOpacityTransferFunction('omega_bz')
omega_bzPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5001220703125, 1.0, 0.5, 0.0]
omega_bzPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'CellDimension'
cellDimensionPWF = GetOpacityTransferFunction('CellDimension')
cellDimensionPWF.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]
cellDimensionPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# restore active source
SetActiveSource(tTKMorseSmaleComplex1)
# ----------------------------------------------------------------


if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')
