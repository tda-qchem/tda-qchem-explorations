#!/usr/bin/env python

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
renderView1.ViewSize = [1373, 564]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.CenterOfRotation = [0.0, -1e-20, 0.0]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [0.7683676928830725, 20.161084688194897, 4.338376735358313]
renderView1.CameraFocalPoint = [0.0, -1e-20, 0.0]
renderView1.CameraViewUp = [-0.004325922102125578, -0.2102106696757141, 0.9776465418301516]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 7.820080520075376
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView10 = CreateView('RenderView')
renderView10.ViewSize = [750, 563]
renderView10.AxesGrid = 'GridAxes3DActor'
renderView10.OrientationAxesVisibility = 0
renderView10.CenterOfRotation = [0.0, -1e-20, 0.0]
renderView10.StereoType = 'Crystal Eyes'
renderView10.CameraPosition = [-0.48610571363436184, 21.14156439337225, 5.938616165787505]
renderView10.CameraFocalPoint = [-0.02574804975648673, -2.7045705873596004, -1.4561547569497613]
renderView10.CameraViewUp = [-0.0029610111817006558, -0.2962398448439609, 0.9551089920734742]
renderView10.CameraFocalDisk = 1.0
renderView10.CameraParallelScale = 7.820080520075376
renderView10.UseColorPaletteForBackground = 0
renderView10.Background = [1.0, 1.0, 1.0]
renderView10.BackEnd = 'OSPRay raycaster'
renderView10.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView11 = CreateView('RenderView')
renderView11.ViewSize = [750, 563]
renderView11.AxesGrid = 'GridAxes3DActor'
renderView11.OrientationAxesVisibility = 0
renderView11.CenterOfRotation = [0.0, 0.0, 3.266334533691406e-05]
renderView11.StereoType = 'Crystal Eyes'
renderView11.CameraPosition = [-0.5812353241563424, 19.77286197873074, 6.151246431197295]
renderView11.CameraFocalPoint = [-0.08434227887015533, 0.22457085524336867, -0.6514562728539224]
renderView11.CameraViewUp = [0.00802853791612718, -0.3284700936942724, 0.9444802486698202]
renderView11.CameraFocalDisk = 1.0
renderView11.CameraParallelScale = 7.845545096214063
renderView11.UseColorPaletteForBackground = 0
renderView11.Background = [1.0, 1.0, 1.0]
renderView11.BackEnd = 'OSPRay raycaster'
renderView11.Shadows = 1
renderView11.AmbientSamples = 4
renderView11.SamplesPerPixel = 4
renderView11.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView12 = CreateView('RenderView')
renderView12.ViewSize = [1510, 1172]
renderView12.InteractionMode = '2D'
renderView12.AxesGrid = 'GridAxes3DActor'
renderView12.OrientationAxesVisibility = 0
renderView12.StereoType = 'Crystal Eyes'
renderView12.CameraPosition = [0.0, 0.0, 37.50561681626333]
renderView12.CameraViewUp = [4.440892098500626e-16, -1.0, 0.0]
renderView12.CameraFocalDisk = 1.0
renderView12.CameraParallelScale = 4.5284654804511275
renderView12.UseColorPaletteForBackground = 0
renderView12.Background = [1.0, 1.0, 1.0]
renderView12.BackEnd = 'OSPRay raycaster'
renderView12.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView13 = CreateView('RenderView')
renderView13.ViewSize = [1510, 1172]
renderView13.InteractionMode = '2D'
renderView13.AxesGrid = 'GridAxes3DActor'
renderView13.OrientationAxesVisibility = 0
renderView13.CenterOfRotation = [1.8272385756993126, 0.0, 0.0]
renderView13.StereoType = 'Crystal Eyes'
renderView13.CameraPosition = [42.99788415425163, 0.0, 0.0]
renderView13.CameraFocalPoint = [1.8272385756993126, 0.0, 0.0]
renderView13.CameraViewUp = [0.0, 0.0, 1.0]
renderView13.CameraFocalDisk = 1.0
renderView13.CameraParallelScale = 4.576017953063724
renderView13.UseColorPaletteForBackground = 0
renderView13.Background = [1.0, 1.0, 1.0]
renderView13.BackEnd = 'OSPRay raycaster'
renderView13.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView14 = CreateView('RenderView')
renderView14.ViewSize = [1510, 1172]
renderView14.InteractionMode = '2D'
renderView14.AxesGrid = 'GridAxes3DActor'
renderView14.OrientationAxesVisibility = 0
renderView14.CenterOfRotation = [0.0, -1.8043497209164818, 0.0]
renderView14.StereoType = 'Crystal Eyes'
renderView14.CameraPosition = [0.0, 38.67053788412107, 0.0]
renderView14.CameraFocalPoint = [0.0, -1.8043497209164818, 0.0]
renderView14.CameraViewUp = [1.0, 0.0, 0.0]
renderView14.CameraFocalDisk = 1.0
renderView14.CameraParallelScale = 5.9132436086409985
renderView14.UseColorPaletteForBackground = 0
renderView14.Background = [1.0, 1.0, 1.0]
renderView14.BackEnd = 'OSPRay raycaster'
renderView14.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView2 = CreateView('RenderView')
renderView2.ViewSize = [750, 563]
renderView2.AxesGrid = 'GridAxes3DActor'
renderView2.OrientationAxesVisibility = 0
renderView2.CenterOfRotation = [0.0, -1e-20, 0.0]
renderView2.StereoType = 'Crystal Eyes'
renderView2.CameraPosition = [-0.48610571363436184, 21.14156439337225, 5.938616165787505]
renderView2.CameraFocalPoint = [-0.02574804975648673, -2.7045705873596004, -1.4561547569497613]
renderView2.CameraViewUp = [-0.0029610111817006558, -0.2962398448439609, 0.9551089920734742]
renderView2.CameraFocalDisk = 1.0
renderView2.CameraParallelScale = 7.820080520075376
renderView2.UseColorPaletteForBackground = 0
renderView2.Background = [1.0, 1.0, 1.0]
renderView2.BackEnd = 'OSPRay raycaster'
renderView2.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView3 = CreateView('RenderView')
renderView3.ViewSize = [682, 563]
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

# Create a new 'Render View'
renderView4 = CreateView('RenderView')
renderView4.ViewSize = [681, 563]
renderView4.AxesGrid = 'GridAxes3DActor'
renderView4.OrientationAxesVisibility = 0
renderView4.CenterOfRotation = [0.0, -1e-20, 0.0]
renderView4.StereoType = 'Crystal Eyes'
renderView4.CameraPosition = [0.0, 20.636890206955403, 0.0]
renderView4.CameraFocalPoint = [0.0, -1e-20, 0.0]
renderView4.CameraViewUp = [0.0, 0.0, 1.0]
renderView4.CameraFocalDisk = 1.0
renderView4.CameraParallelScale = 7.820080520075376
renderView4.BackEnd = 'OSPRay raycaster'
renderView4.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView5 = CreateView('RenderView')
renderView5.ViewSize = [750, 564]
renderView5.AxesGrid = 'GridAxes3DActor'
renderView5.OrientationAxesVisibility = 0
renderView5.CenterOfRotation = [0.0, 0.0, 3.266334533691406e-05]
renderView5.StereoType = 'Crystal Eyes'
renderView5.CameraPosition = [-0.5812353241563424, 19.77286197873074, 6.151246431197295]
renderView5.CameraFocalPoint = [-0.08434227887015533, 0.22457085524336867, -0.6514562728539224]
renderView5.CameraViewUp = [0.00802853791612718, -0.3284700936942724, 0.9444802486698202]
renderView5.CameraFocalDisk = 1.0
renderView5.CameraParallelScale = 7.845545096214063
renderView5.UseColorPaletteForBackground = 0
renderView5.Background = [1.0, 1.0, 1.0]
renderView5.BackEnd = 'OSPRay raycaster'
renderView5.Shadows = 1
renderView5.AmbientSamples = 4
renderView5.SamplesPerPixel = 4
renderView5.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView6 = CreateView('RenderView')
renderView6.ViewSize = [750, 564]
renderView6.AxesGrid = 'GridAxes3DActor'
renderView6.OrientationAxesVisibility = 0
renderView6.CenterOfRotation = [0.7125580310821533, 0.0, 0.0]
renderView6.StereoType = 'Crystal Eyes'
renderView6.CameraPosition = [1.8567215175885559, 6.49947558261868, 0.09456697029865793]
renderView6.CameraFocalPoint = [1.0041010884536372, -0.037442552411962905, -0.030513653439580894]
renderView6.CameraViewUp = [0.015946314931483005, -0.021207660170597074, 0.9996479131125091]
renderView6.CameraFocalDisk = 1.0
renderView6.CameraParallelScale = 11.743275661962203
renderView6.UseColorPaletteForBackground = 0
renderView6.Background = [1.0, 1.0, 1.0]
renderView6.BackEnd = 'OSPRay raycaster'
renderView6.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView7 = CreateView('RenderView')
renderView7.ViewSize = [750, 563]
renderView7.AxesGrid = 'GridAxes3DActor'
renderView7.OrientationAxesVisibility = 0
renderView7.StereoType = 'Crystal Eyes'
renderView7.CameraPosition = [-0.23141696055091165, 11.655813358411772, 0.2895578809896814]
renderView7.CameraFocalPoint = [-0.5359189544348181, 0.01715308415166948, -0.09482796784114833]
renderView7.CameraViewUp = [0.003848458683573176, -0.03310897599412297, 0.9994443381571491]
renderView7.CameraFocalDisk = 1.0
renderView7.CameraParallelScale = 7.820080520075376
renderView7.UseColorPaletteForBackground = 0
renderView7.Background = [1.0, 1.0, 1.0]
renderView7.BackEnd = 'OSPRay raycaster'
renderView7.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView8 = CreateView('RenderView')
renderView8.ViewSize = [750, 564]
renderView8.AxesGrid = 'GridAxes3DActor'
renderView8.OrientationAxesVisibility = 0
renderView8.CenterOfRotation = [0.0, -1e-20, 0.0]
renderView8.StereoType = 'Crystal Eyes'
renderView8.CameraPosition = [-0.48610571363436184, 21.14156439337225, 5.938616165787505]
renderView8.CameraFocalPoint = [-0.02574804975648673, -2.7045705873596004, -1.4561547569497613]
renderView8.CameraViewUp = [-0.0029610111817006558, -0.2962398448439609, 0.9551089920734742]
renderView8.CameraFocalDisk = 1.0
renderView8.CameraParallelScale = 7.820080520075376
renderView8.UseColorPaletteForBackground = 0
renderView8.Background = [1.0, 1.0, 1.0]
renderView8.BackEnd = 'OSPRay raycaster'
renderView8.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView9 = CreateView('RenderView')
renderView9.ViewSize = [750, 564]
renderView9.AxesGrid = 'GridAxes3DActor'
renderView9.OrientationAxesVisibility = 0
renderView9.CenterOfRotation = [0.49936618737029903, 0.5000009768371569, 0.0]
renderView9.StereoType = 'Crystal Eyes'
renderView9.CameraPosition = [0.49936618737029903, 0.5000009768371569, 2.2564602931646442]
renderView9.CameraFocalPoint = [0.49936618737029903, 0.5000009768371569, 0.0]
renderView9.CameraFocalDisk = 1.0
renderView9.CameraParallelScale = 0.7066580270502391
renderView9.UseColorPaletteForBackground = 0
renderView9.Background = [1.0, 1.0, 1.0]
renderView9.BackEnd = 'OSPRay raycaster'
renderView9.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Input Data'
inputData = CreateLayout(name='Input Data')
inputData.SplitHorizontal(0, 0.500000)
inputData.SplitVertical(1, 0.500000)
inputData.AssignView(3, renderView5)
inputData.AssignView(4, renderView11)
inputData.SplitVertical(2, 0.500000)
inputData.AssignView(5, renderView6)
inputData.AssignView(6, renderView7)
inputData.SetSize(1501, 1128)

# create new layout object 'LIC Texture Back'
lICTextureBack = CreateLayout(name='LIC Texture Back')
lICTextureBack.AssignView(0, renderView14)
lICTextureBack.SetSize(1510, 1172)

# create new layout object 'LIC Texture Bottom'
lICTextureBottom = CreateLayout(name='LIC Texture Bottom')
lICTextureBottom.AssignView(0, renderView12)
lICTextureBottom.SetSize(1510, 1172)

# create new layout object 'LIC Texture Side'
lICTextureSide = CreateLayout(name='LIC Texture Side')
lICTextureSide.AssignView(0, renderView13)
lICTextureSide.SetSize(1510, 1172)

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.SplitVertical(0, 0.500000)
layout1.AssignView(1, renderView1)
layout1.SplitHorizontal(2, 0.500000)
layout1.AssignView(5, renderView3)
layout1.AssignView(6, renderView4)
layout1.SetSize(1373, 1128)

# create new layout object 'Topological Analysis'
topologicalAnalysis = CreateLayout(name='Topological Analysis')
topologicalAnalysis.SplitHorizontal(0, 0.500000)
topologicalAnalysis.SplitVertical(1, 0.500000)
topologicalAnalysis.AssignView(3, renderView8)
topologicalAnalysis.AssignView(4, renderView10)
topologicalAnalysis.SplitVertical(2, 0.500000)
topologicalAnalysis.AssignView(5, renderView9)
topologicalAnalysis.AssignView(6, renderView2)
topologicalAnalysis.SetSize(1501, 1128)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView9)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'XML Image Data Reader'
start_data_bzvti = XMLImageDataReader(registrationName='start_data_bz.vti', FileName=['data/LiH_MICD/vti/start_data_bz.vti'])
start_data_bzvti.PointArrayStatus = ['bz_jx', 'bz_jy', 'bz_jz']
start_data_bzvti.TimeArray = 'None'

# create a new 'XML Image Data Reader'
start_data_omega_bzvti = XMLImageDataReader(registrationName='start_data_omega_bz.vti', FileName=['data/LiH_MICD/vti/start_data_omega_bz.vti'])
start_data_omega_bzvti.CellArrayStatus = ['vtkGhostType']
start_data_omega_bzvti.PointArrayStatus = ['bz_wz', 'omega_bz', 'vtkValidPointMask', 'vtkGhostType']
start_data_omega_bzvti.TimeArray = 'None'

# create a new 'Contour'
contour4 = Contour(registrationName='Contour4', Input=start_data_omega_bzvti)
contour4.ContourBy = ['POINTS', 'omega_bz']
contour4.Isosurfaces = [0.996]
contour4.PointMergeMethod = 'Uniform Binning'

# create a new 'Contour'
contour2 = Contour(registrationName='Contour2', Input=start_data_omega_bzvti)
contour2.ContourBy = ['POINTS', 'omega_bz']
contour2.Isosurfaces = [0.8]
contour2.PointMergeMethod = 'Uniform Binning'

# create a new 'Connectivity'
connectivity2 = Connectivity(registrationName='Connectivity2', Input=contour2)

# create a new 'Append Attributes'
appendAttributes1 = AppendAttributes(registrationName='AppendAttributes1', Input=[start_data_bzvti, start_data_omega_bzvti])

# create a new 'Calculator'
calculator2 = Calculator(registrationName='Calculator2', Input=appendAttributes1)
calculator2.ResultArrayName = 'Bz'
calculator2.Function = 'bz_jx*iHat+bz_jy*jHat+bz_jz*kHat'

# create a new 'Slice'
slice3 = Slice(registrationName='Slice3', Input=calculator2)
slice3.SliceType = 'Plane'
slice3.HyperTreeGridSlicer = 'Plane'
slice3.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice3.SliceType.Origin = [0.0, -3.0421146784507793, 0.0]
slice3.SliceType.Normal = [0.0, 1.0, 0.0]

# create a new 'Calculator'
calculator7 = Calculator(registrationName='Calculator7', Input=slice3)
calculator7.ResultArrayName = 'v'
calculator7.Function = 'coordsX'

# create a new 'Calculator'
calculator8 = Calculator(registrationName='Calculator8', Input=calculator7)
calculator8.ResultArrayName = 'u'
calculator8.Function = 'coordsZ'

# create a new 'TTK TextureMapFromField'
tTKTextureMapFromField3 = TTKTextureMapFromField(registrationName='TTKTextureMapFromField3', Input=calculator8)
tTKTextureMapFromField3.OnlyUComponent = 0
tTKTextureMapFromField3.UComponent = ['POINTS', 'u']
tTKTextureMapFromField3.VComponent = ['POINTS', 'v']

# create a new 'Stream Tracer'
streamTracer2 = StreamTracer(registrationName='StreamTracer2', Input=calculator2,
    SeedType='Line')
streamTracer2.Vectors = ['POINTS', 'Bz']
streamTracer2.MaximumStreamlineLength = 10.061825318164619

# init the 'Line' selected for 'SeedType'
streamTracer2.SeedType.Point1 = [-3.8535974531291313, -0.2632180773499126, -4.601697315219196]
streamTracer2.SeedType.Point2 = [-3.8535974531291313, -0.2632180773499126, 3.8651295979454225]
streamTracer2.SeedType.Resolution = 25

# create a new 'Tube'
tube5 = Tube(registrationName='Tube5', Input=streamTracer2)
tube5.Scalars = ['POINTS', 'AngularVelocity']
tube5.Vectors = ['POINTS', 'Normals']
tube5.Radius = 0.01

# create a new 'Slice'
slice1 = Slice(registrationName='Slice1', Input=calculator2)
slice1.SliceType = 'Plane'
slice1.HyperTreeGridSlicer = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [0.0, 0.0, -2.9248158671542552]
slice1.SliceType.Normal = [0.0, 0.0, 1.0]

# create a new 'Slice'
slice2 = Slice(registrationName='Slice2', Input=calculator2)
slice2.SliceType = 'Plane'
slice2.HyperTreeGridSlicer = 'Plane'
slice2.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice2.SliceType.Origin = [4.044891431016442, 0.0, 0.0]

# create a new 'Calculator'
calculator3 = Calculator(registrationName='Calculator3', Input=slice1)
calculator3.ResultArrayName = 'x'
calculator3.Function = '-coordsX'

# create a new 'Calculator'
calculator4 = Calculator(registrationName='Calculator4', Input=calculator3)
calculator4.ResultArrayName = 'y'
calculator4.Function = 'coordsY'

# create a new 'TTK ScalarFieldNormalizer'
tTKScalarFieldNormalizer1 = TTKScalarFieldNormalizer(registrationName='TTKScalarFieldNormalizer1', Input=start_data_omega_bzvti)
tTKScalarFieldNormalizer1.ScalarField = ['POINTS', 'omega_bz']

# create a new 'TTK TopologicalSimplificationByPersistence'
tTKTopologicalSimplificationByPersistence1 = TTKTopologicalSimplificationByPersistence(registrationName='TTKTopologicalSimplificationByPersistence1', Input=tTKScalarFieldNormalizer1)
tTKTopologicalSimplificationByPersistence1.InputArray = ['POINTS', 'omega_bz']
tTKTopologicalSimplificationByPersistence1.PersistenceThreshold = 0.3

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram1', Input=tTKScalarFieldNormalizer1)
tTKPersistenceDiagram1.ScalarField = ['POINTS', 'omega_bz']
tTKPersistenceDiagram1.InputOffsetField = ['POINTS', 'bz_wz']

# create a new 'Threshold'
threshold12 = Threshold(registrationName='Threshold12', Input=tTKPersistenceDiagram1)
threshold12.Scalars = ['CELLS', 'PairIdentifier']
threshold12.LowerThreshold = -0.1
threshold12.UpperThreshold = 99999.0

# create a new 'Threshold'
threshold10 = Threshold(registrationName='Threshold10', Input=threshold12)
threshold10.Scalars = ['CELLS', 'Persistence']
threshold10.LowerThreshold = 0.3
threshold10.UpperThreshold = 1.9999999999999998

# create a new 'Extract Surface'
extractSurface3 = ExtractSurface(registrationName='ExtractSurface3', Input=threshold10)

# create a new 'Tube'
tube3 = Tube(registrationName='Tube3', Input=extractSurface3)
tube3.Scalars = ['POINTS', '']
tube3.Vectors = ['POINTS', 'Coordinates']
tube3.Radius = 0.01

# create a new 'TTK IcospheresFromPoints'
tTKIcospheresFromPoints3 = TTKIcospheresFromPoints(registrationName='TTKIcospheresFromPoints3', Input=threshold10)
tTKIcospheresFromPoints3.Radius = 0.025

# create a new 'TTK IcospheresFromPoints'
tTKIcospheresFromPoints4 = TTKIcospheresFromPoints(registrationName='TTKIcospheresFromPoints4', Input=tTKPersistenceDiagram1)
tTKIcospheresFromPoints4.Radius = 0.015

# create a new 'Threshold'
threshold6 = Threshold(registrationName='Threshold6', Input=connectivity2)
threshold6.Scalars = ['POINTS', 'RegionId']
threshold6.LowerThreshold = 1.0
threshold6.UpperThreshold = 1.0

# create a new 'Stream Tracer'
streamTracer1 = StreamTracer(registrationName='StreamTracer1', Input=calculator2,
    SeedType='Line')
streamTracer1.Vectors = ['POINTS', 'Bz']
streamTracer1.MaximumStreamlineLength = 10.061825318164619

# init the 'Line' selected for 'SeedType'
streamTracer1.SeedType.Point1 = [-1.9534905127557192, -0.04254856215702371, -4.218094425531314]
streamTracer1.SeedType.Point2 = [-1.9534905127557192, -0.04254856215702371, 4.248732487633305]
streamTracer1.SeedType.Resolution = 100

# create a new 'Threshold'
threshold11 = Threshold(registrationName='Threshold11', Input=tube3)
threshold11.Scalars = ['CELLS', 'PairIdentifier']
threshold11.LowerThreshold = -0.1
threshold11.UpperThreshold = 190.0

# create a new 'Extract Surface'
extractSurface4 = ExtractSurface(registrationName='ExtractSurface4', Input=tTKPersistenceDiagram1)

# create a new 'Tube'
tube8 = Tube(registrationName='Tube8', Input=extractSurface4)
tube8.Scalars = ['POINTS', 'CriticalType']
tube8.Vectors = ['POINTS', 'Coordinates']
tube8.Radius = 0.0075

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
tTKGeometrySmoother2.InputMaskField = ['POINTS', '']

# create a new 'Threshold'
threshold9 = Threshold(registrationName='Threshold9', Input=tTKPersistenceDiagram1)
threshold9.Scalars = ['CELLS', 'PairIdentifier']
threshold9.LowerThreshold = -1.0
threshold9.UpperThreshold = -0.1

# create a new 'Extract Surface'
extractSurface2 = ExtractSurface(registrationName='ExtractSurface2', Input=threshold9)

# create a new 'Tube'
tube2 = Tube(registrationName='Tube2', Input=extractSurface2)
tube2.Scalars = ['POINTS', '']
tube2.Vectors = ['POINTS', 'Coordinates']
tube2.Radius = 0.01

# create a new 'TTK TextureMapFromField'
tTKTextureMapFromField1 = TTKTextureMapFromField(registrationName='TTKTextureMapFromField1', Input=calculator4)
tTKTextureMapFromField1.OnlyUComponent = 0
tTKTextureMapFromField1.UComponent = ['POINTS', 'x']
tTKTextureMapFromField1.VComponent = ['POINTS', 'y']

# create a new 'Contour'
contour3 = Contour(registrationName='Contour3', Input=start_data_omega_bzvti)
contour3.ContourBy = ['POINTS', 'omega_bz']
contour3.Isosurfaces = [0.92]
contour3.PointMergeMethod = 'Uniform Binning'

# create a new 'Connectivity'
connectivity3 = Connectivity(registrationName='Connectivity3', Input=contour3)

# create a new 'Threshold'
threshold7 = Threshold(registrationName='Threshold7', Input=connectivity3)
threshold7.Scalars = ['POINTS', 'RegionId']
threshold7.LowerThreshold = 1.0
threshold7.UpperThreshold = 2.0

# create a new 'Calculator'
calculator5 = Calculator(registrationName='Calculator5', Input=slice2)
calculator5.ResultArrayName = 'u'
calculator5.Function = 'coordsY'

# create a new 'Calculator'
calculator6 = Calculator(registrationName='Calculator6', Input=calculator5)
calculator6.ResultArrayName = 'v'
calculator6.Function = 'coordsZ'

# create a new 'TTK TextureMapFromField'
tTKTextureMapFromField2 = TTKTextureMapFromField(registrationName='TTKTextureMapFromField2', Input=calculator6)
tTKTextureMapFromField2.OnlyUComponent = 0
tTKTextureMapFromField2.UComponent = ['POINTS', 'u']
tTKTextureMapFromField2.VComponent = ['POINTS', 'v']

# create a new 'Threshold'
threshold8 = Threshold(registrationName='Threshold8', Input=connectivity2)
threshold8.Scalars = ['POINTS', 'RegionId']

# create a new 'Tube'
tube4 = Tube(registrationName='Tube4', Input=streamTracer1)
tube4.Scalars = ['POINTS', 'AngularVelocity']
tube4.Vectors = ['POINTS', 'Normals']
tube4.Radius = 0.05

# create a new 'Contour'
contour1 = Contour(registrationName='Contour1', Input=start_data_omega_bzvti)
contour1.ContourBy = ['POINTS', 'omega_bz']
contour1.Isosurfaces = [0.5]
contour1.PointMergeMethod = 'Uniform Binning'

# create a new 'Connectivity'
connectivity1 = Connectivity(registrationName='Connectivity1', Input=contour1)

# create a new 'Threshold'
threshold4 = Threshold(registrationName='Threshold4', Input=connectivity1)
threshold4.Scalars = ['POINTS', 'RegionId']
threshold4.LowerThreshold = 2.0
threshold4.UpperThreshold = 2.0

# create a new 'Threshold'
threshold5 = Threshold(registrationName='Threshold5', Input=connectivity1)
threshold5.Scalars = ['POINTS', 'RegionId']

# create a new 'TTK MorseSmaleComplex'
tTKMorseSmaleComplex1 = TTKMorseSmaleComplex(registrationName='TTKMorseSmaleComplex1', Input=tTKTopologicalSimplificationByPersistence1)
tTKMorseSmaleComplex1.ScalarField = ['POINTS', 'omega_bz']
tTKMorseSmaleComplex1.OffsetField = ['POINTS', 'bz_wz']
tTKMorseSmaleComplex1.AscendingSegmentation = 0
tTKMorseSmaleComplex1.DescendingSegmentation = 0
tTKMorseSmaleComplex1.MorseSmaleComplexSegmentation = 0
tTKMorseSmaleComplex1.ReturnSaddleConnectors = 1
tTKMorseSmaleComplex1.SaddleConnectorsPersistenceThreshold = 0.3

# create a new 'TTK IcospheresFromPoints'
tTKIcospheresFromPoints2 = TTKIcospheresFromPoints(registrationName='TTKIcospheresFromPoints2', Input=tTKMorseSmaleComplex1)
tTKIcospheresFromPoints2.Radius = 0.175

# find source
tTKMorseSmaleComplex1_1 = FindSource('TTKMorseSmaleComplex1')

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother1 = TTKGeometrySmoother(registrationName='TTKGeometrySmoother1', Input=OutputPort(tTKMorseSmaleComplex1_1,1))
tTKGeometrySmoother1.IterationNumber = 1000
tTKGeometrySmoother1.InputMaskField = ['CELLS', 'SeparatrixType']

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(registrationName='ExtractSurface1', Input=tTKGeometrySmoother1)

# create a new 'Tube'
tube1 = Tube(registrationName='Tube1', Input=extractSurface1)
tube1.Scalars = ['POINTS', '']
tube1.Vectors = ['POINTS', '1']
tube1.Radius = 0.05

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

# create a new 'Glyph'
glyph1 = Glyph(registrationName='Glyph1', Input=streamTracer1,
    GlyphType='Cone')
glyph1.OrientationArray = ['POINTS', 'Bz']
glyph1.ScaleArray = ['POINTS', 'No scale array']
glyph1.ScaleFactor = 0.8382161617279054
glyph1.GlyphTransform = 'Transform2'
glyph1.GlyphMode = 'Every Nth Point'
glyph1.MaximumNumberOfSamplePoints = 2000
glyph1.Stride = 50

# init the 'Cone' selected for 'GlyphType'
glyph1.GlyphType.Resolution = 20
glyph1.GlyphType.Radius = 0.25
glyph1.GlyphType.Height = 0.5

# create a new 'TTK DiscreteGradient'
tTKDiscreteGradient1 = TTKDiscreteGradient(registrationName='TTKDiscreteGradient1', Input=start_data_omega_bzvti)
tTKDiscreteGradient1.ScalarField = ['POINTS', 'omega_bz']
tTKDiscreteGradient1.OffsetField = ['POINTS', 'bz_wz']
tTKDiscreteGradient1.ComputeGradientGlyphs = 0

# create a new 'TTK IcospheresFromPoints'
tTKIcospheresFromPoints1 = TTKIcospheresFromPoints(registrationName='TTKIcospheresFromPoints1', Input=tTKDiscreteGradient1)
tTKIcospheresFromPoints1.Radius = 0.175

# create a new 'Transform'
transform1 = Transform(registrationName='Transform1', Input=tTKGeometrySmoother2)
transform1.Transform = 'Transform'

# init the 'Transform' selected for 'Transform'
transform1.Transform.Translate = [0.05, 0.0, 0.0]
transform1.Transform.Scale = [1.3, 1.3, 1.3]

# create a new 'Stream Tracer With Custom Source'
streamTracerWithCustomSource1 = StreamTracerWithCustomSource(registrationName='StreamTracerWithCustomSource1', Input=calculator2,
    SeedSource=transform1)
streamTracerWithCustomSource1.Vectors = ['POINTS', 'Bz']
streamTracerWithCustomSource1.MaximumStreamlineLength = 10.061825318164619

# create a new 'Tube'
tube7 = Tube(registrationName='Tube7', Input=streamTracerWithCustomSource1)
tube7.Scalars = ['POINTS', 'AngularVelocity']
tube7.Vectors = ['POINTS', 'Normals']
tube7.Radius = 0.05

# create a new 'Transform'
transform2 = Transform(registrationName='Transform2', Input=transform1)
transform2.Transform = 'Transform'

# init the 'Transform' selected for 'Transform'
transform2.Transform.Translate = [-0.4, 0.0, 0.0]
transform2.Transform.Scale = [1.9, 1.9, 1.85]

# create a new 'Stream Tracer With Custom Source'
streamTracerWithCustomSource2 = StreamTracerWithCustomSource(registrationName='StreamTracerWithCustomSource2', Input=calculator2,
    SeedSource=transform2)
streamTracerWithCustomSource2.Vectors = ['POINTS', 'Bz']
streamTracerWithCustomSource2.MaximumStreamlineLength = 10.061825318164619

# create a new 'Tube'
tube6 = Tube(registrationName='Tube6', Input=streamTracerWithCustomSource2)
tube6.Scalars = ['POINTS', 'AngularVelocity']
tube6.Vectors = ['POINTS', 'Normals']
tube6.Radius = 0.01

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from contour1
contour1Display = Show(contour1, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'omega_bz'
omega_bzLUT = GetColorTransferFunction('omega_bz')
omega_bzLUT.RGBPoints = [0.49758370749999525, 0.0, 0.129412, 0.584314, 0.7307818610184227, 0.917647, 0.941176, 0.788235, 0.9639800145368502, 0.0, 0.431373, 0.0]
omega_bzLUT.ColorSpace = 'RGB'
omega_bzLUT.AboveRangeColor = [1.0, 1.0, 1.0]
omega_bzLUT.NanColor = [0.0, 0.0, 0.0]
omega_bzLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
contour1Display.Representation = 'Surface'
contour1Display.ColorArrayName = ['POINTS', '']
contour1Display.LookupTable = omega_bzLUT
contour1Display.Opacity = 0.3
contour1Display.Specular = 1.0
contour1Display.SelectTCoordArray = 'None'
contour1Display.SelectNormalArray = 'Normals'
contour1Display.SelectTangentArray = 'None'
contour1Display.EdgeColor = [0.0, 0.0, 0.0]
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
tTKMorseSmaleComplex1Display.EdgeColor = [0.0, 0.0, 0.0]
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
tTKMorseSmaleComplex1_2Display.ColorArrayName = ['POINTS', '']
tTKMorseSmaleComplex1_2Display.Specular = 1.0
tTKMorseSmaleComplex1_2Display.SelectTCoordArray = 'None'
tTKMorseSmaleComplex1_2Display.SelectNormalArray = 'None'
tTKMorseSmaleComplex1_2Display.SelectTangentArray = 'None'
tTKMorseSmaleComplex1_2Display.EdgeColor = [0.0, 0.0, 0.0]
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
tTKGeometrySmoother1Display.EdgeColor = [0.0, 0.0, 0.0]
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
# setup the visualization in view 'renderView10'
# ----------------------------------------------------------------

# show data from start_data_omega_bzvti
start_data_omega_bzvtiDisplay = Show(start_data_omega_bzvti, renderView10, 'UniformGridRepresentation')

# trace defaults for the display properties.
start_data_omega_bzvtiDisplay.Representation = 'Outline'
start_data_omega_bzvtiDisplay.AmbientColor = [0.1803921568627451, 0.17647058823529413, 0.17647058823529413]
start_data_omega_bzvtiDisplay.ColorArrayName = ['POINTS', '']
start_data_omega_bzvtiDisplay.DiffuseColor = [0.1803921568627451, 0.17647058823529413, 0.17647058823529413]
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
contour1Display_1 = Show(contour1, renderView10, 'GeometryRepresentation')

# trace defaults for the display properties.
contour1Display_1.Representation = 'Surface'
contour1Display_1.ColorArrayName = ['POINTS', '']
contour1Display_1.LookupTable = omega_bzLUT
contour1Display_1.Opacity = 0.2
contour1Display_1.Specular = 1.0
contour1Display_1.SelectTCoordArray = 'None'
contour1Display_1.SelectNormalArray = 'Normals'
contour1Display_1.SelectTangentArray = 'None'
contour1Display_1.EdgeColor = [0.0, 0.0, 0.0]
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

# show data from tTKIcospheresFromPoints2
tTKIcospheresFromPoints2Display = Show(tTKIcospheresFromPoints2, renderView10, 'GeometryRepresentation')

# trace defaults for the display properties.
tTKIcospheresFromPoints2Display.Representation = 'Surface'
tTKIcospheresFromPoints2Display.ColorArrayName = ['POINTS', 'CellDimension']
tTKIcospheresFromPoints2Display.LookupTable = cellDimensionLUT
tTKIcospheresFromPoints2Display.Specular = 1.0
tTKIcospheresFromPoints2Display.SelectTCoordArray = 'None'
tTKIcospheresFromPoints2Display.SelectNormalArray = 'Normals'
tTKIcospheresFromPoints2Display.SelectTangentArray = 'None'
tTKIcospheresFromPoints2Display.EdgeColor = [0.0, 0.0, 0.0]
tTKIcospheresFromPoints2Display.OSPRayScaleArray = 'CellDimension'
tTKIcospheresFromPoints2Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKIcospheresFromPoints2Display.SelectOrientationVectors = 'None'
tTKIcospheresFromPoints2Display.ScaleFactor = 0.866682767868042
tTKIcospheresFromPoints2Display.SelectScaleArray = 'CellDimension'
tTKIcospheresFromPoints2Display.GlyphType = 'Arrow'
tTKIcospheresFromPoints2Display.GlyphTableIndexArray = 'CellDimension'
tTKIcospheresFromPoints2Display.GaussianRadius = 0.043334138393402104
tTKIcospheresFromPoints2Display.SetScaleArray = ['POINTS', 'CellDimension']
tTKIcospheresFromPoints2Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKIcospheresFromPoints2Display.OpacityArray = ['POINTS', 'CellDimension']
tTKIcospheresFromPoints2Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKIcospheresFromPoints2Display.DataAxesGrid = 'GridAxesRepresentation'
tTKIcospheresFromPoints2Display.PolarAxes = 'PolarAxesRepresentation'
tTKIcospheresFromPoints2Display.SelectInputVectors = ['POINTS', 'CellDimension']
tTKIcospheresFromPoints2Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKIcospheresFromPoints2Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKIcospheresFromPoints2Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKIcospheresFromPoints2Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# ----------------------------------------------------------------
# setup the visualization in view 'renderView11'
# ----------------------------------------------------------------

# show data from start_data_omega_bzvti
start_data_omega_bzvtiDisplay_1 = Show(start_data_omega_bzvti, renderView11, 'UniformGridRepresentation')

# trace defaults for the display properties.
start_data_omega_bzvtiDisplay_1.Representation = 'Outline'
start_data_omega_bzvtiDisplay_1.AmbientColor = [0.1803921568627451, 0.17647058823529413, 0.17647058823529413]
start_data_omega_bzvtiDisplay_1.ColorArrayName = [None, '']
start_data_omega_bzvtiDisplay_1.DiffuseColor = [0.1803921568627451, 0.17647058823529413, 0.17647058823529413]
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

# show data from start_data_bzvti
start_data_bzvtiDisplay = Show(start_data_bzvti, renderView11, 'UniformGridRepresentation')

# trace defaults for the display properties.
start_data_bzvtiDisplay.Representation = 'Outline'
start_data_bzvtiDisplay.ColorArrayName = [None, '']
start_data_bzvtiDisplay.SelectTCoordArray = 'None'
start_data_bzvtiDisplay.SelectNormalArray = 'None'
start_data_bzvtiDisplay.SelectTangentArray = 'None'
start_data_bzvtiDisplay.OSPRayScaleArray = 'bz_jx'
start_data_bzvtiDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
start_data_bzvtiDisplay.SelectOrientationVectors = 'None'
start_data_bzvtiDisplay.ScaleFactor = 1.006182531816462
start_data_bzvtiDisplay.SelectScaleArray = 'None'
start_data_bzvtiDisplay.GlyphType = 'Arrow'
start_data_bzvtiDisplay.GlyphTableIndexArray = 'None'
start_data_bzvtiDisplay.GaussianRadius = 0.050309126590823094
start_data_bzvtiDisplay.SetScaleArray = ['POINTS', 'bz_jx']
start_data_bzvtiDisplay.ScaleTransferFunction = 'PiecewiseFunction'
start_data_bzvtiDisplay.OpacityArray = ['POINTS', 'bz_jx']
start_data_bzvtiDisplay.OpacityTransferFunction = 'PiecewiseFunction'
start_data_bzvtiDisplay.DataAxesGrid = 'GridAxesRepresentation'
start_data_bzvtiDisplay.PolarAxes = 'PolarAxesRepresentation'
start_data_bzvtiDisplay.ScalarOpacityUnitDistance = 0.12315087617612483
start_data_bzvtiDisplay.OpacityArrayName = ['POINTS', 'bz_jx']
start_data_bzvtiDisplay.SliceFunction = 'Plane'
start_data_bzvtiDisplay.Slice = 63
start_data_bzvtiDisplay.SelectInputVectors = ['POINTS', 'bz_jx']
start_data_bzvtiDisplay.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
start_data_bzvtiDisplay.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
start_data_bzvtiDisplay.ScaleTransferFunction.Points = [-0.4143731235557371, 0.0, 0.5, 0.0, 0.41437312355573663, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
start_data_bzvtiDisplay.OpacityTransferFunction.Points = [-0.4143731235557371, 0.0, 0.5, 0.0, 0.41437312355573663, 1.0, 0.5, 0.0]

# show data from calculator2
calculator2Display = Show(calculator2, renderView11, 'UniformGridRepresentation')

# get color transfer function/color map for 'Bz'
bzLUT = GetColorTransferFunction('Bz')
bzLUT.RGBPoints = [7.36291008310002e-06, 0.0, 0.129412, 0.584314, 0.23463837802410126, 0.39215686274509803, 0.47843137254901963, 0.6705882352941176, 0.3288603056261099, 0.8666666666666667, 0.8980392156862745, 0.7764705882352941, 0.5782711991474931, 0.0, 0.431373, 0.0]
bzLUT.ColorSpace = 'RGB'
bzLUT.AboveRangeColor = [1.0, 1.0, 1.0]
bzLUT.NanColor = [0.0, 0.0, 0.0]
bzLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'Bz'
bzPWF = GetOpacityTransferFunction('Bz')
bzPWF.Points = [7.36291008310002e-06, 0.0, 0.5, 0.0, 0.3307077884674072, 0.6556016802787781, 0.5, 0.0, 0.5782711991474931, 1.0, 0.5, 0.0]
bzPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
calculator2Display.Representation = 'Volume'
calculator2Display.ColorArrayName = ['POINTS', 'Bz']
calculator2Display.LookupTable = bzLUT
calculator2Display.SelectTCoordArray = 'None'
calculator2Display.SelectNormalArray = 'None'
calculator2Display.SelectTangentArray = 'None'
calculator2Display.OSPRayScaleArray = 'Bz'
calculator2Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator2Display.SelectOrientationVectors = 'Bz'
calculator2Display.ScaleFactor = 1.006182531816462
calculator2Display.SelectScaleArray = 'Bz'
calculator2Display.GlyphType = 'Arrow'
calculator2Display.GlyphTableIndexArray = 'Bz'
calculator2Display.GaussianRadius = 0.050309126590823094
calculator2Display.SetScaleArray = ['POINTS', 'Bz']
calculator2Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator2Display.OpacityArray = ['POINTS', 'Bz']
calculator2Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator2Display.DataAxesGrid = 'GridAxesRepresentation'
calculator2Display.PolarAxes = 'PolarAxesRepresentation'
calculator2Display.ScalarOpacityUnitDistance = 0.12315087617612483
calculator2Display.ScalarOpacityFunction = bzPWF
calculator2Display.OpacityArrayName = ['POINTS', 'Bz']
calculator2Display.SliceFunction = 'Plane'
calculator2Display.Slice = 63
calculator2Display.SelectInputVectors = ['POINTS', 'Bz']
calculator2Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
calculator2Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator2Display.ScaleTransferFunction.Points = [-0.4143731235557371, 0.0, 0.5, 0.0, 0.41437312355573663, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator2Display.OpacityTransferFunction.Points = [-0.4143731235557371, 0.0, 0.5, 0.0, 0.41437312355573663, 1.0, 0.5, 0.0]

# show data from slice1
slice1Display = Show(slice1, renderView11, 'GeometryRepresentation')

# trace defaults for the display properties.
slice1Display.Representation = 'Surface LIC'
slice1Display.ColorArrayName = ['POINTS', 'Bz']
slice1Display.LookupTable = bzLUT
slice1Display.Specular = 1.0
slice1Display.SelectTCoordArray = 'None'
slice1Display.SelectNormalArray = 'None'
slice1Display.SelectTangentArray = 'None'
slice1Display.EdgeColor = [0.0, 0.0, 0.0]
slice1Display.OSPRayScaleArray = 'Bz'
slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice1Display.SelectOrientationVectors = 'Bz'
slice1Display.ScaleFactor = 1.0061825752258302
slice1Display.SelectScaleArray = 'Bz'
slice1Display.GlyphType = 'Arrow'
slice1Display.GlyphTableIndexArray = 'Bz'
slice1Display.GaussianRadius = 0.050309128761291504
slice1Display.SetScaleArray = ['POINTS', 'Bz']
slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
slice1Display.OpacityArray = ['POINTS', 'Bz']
slice1Display.OpacityTransferFunction = 'PiecewiseFunction'
slice1Display.DataAxesGrid = 'GridAxesRepresentation'
slice1Display.PolarAxes = 'PolarAxesRepresentation'
slice1Display.SelectInputVectors = ['POINTS', 'Bz']
slice1Display.EnhanceContrast = 'Color Only'
slice1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
slice1Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice1Display.ScaleTransferFunction.Points = [-4.99999930347883e-10, 0.0, 0.5, 0.0, 5.000000136146099e-10, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice1Display.OpacityTransferFunction.Points = [-4.99999930347883e-10, 0.0, 0.5, 0.0, 5.000000136146099e-10, 1.0, 0.5, 0.0]

# show data from contour1
contour1Display_2 = Show(contour1, renderView11, 'GeometryRepresentation')

# trace defaults for the display properties.
contour1Display_2.Representation = 'Surface'
contour1Display_2.ColorArrayName = ['POINTS', 'omega_bz']
contour1Display_2.LookupTable = omega_bzLUT
contour1Display_2.Opacity = 0.3
contour1Display_2.Specular = 1.0
contour1Display_2.SelectTCoordArray = 'None'
contour1Display_2.SelectNormalArray = 'Normals'
contour1Display_2.SelectTangentArray = 'None'
contour1Display_2.EdgeColor = [0.0, 0.0, 0.0]
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

# show data from streamTracer1
streamTracer1Display = Show(streamTracer1, renderView11, 'GeometryRepresentation')

# trace defaults for the display properties.
streamTracer1Display.Representation = 'Surface'
streamTracer1Display.ColorArrayName = [None, '']
streamTracer1Display.Specular = 1.0
streamTracer1Display.SelectTCoordArray = 'None'
streamTracer1Display.SelectNormalArray = 'None'
streamTracer1Display.SelectTangentArray = 'None'
streamTracer1Display.EdgeColor = [0.0, 0.0, 0.0]
streamTracer1Display.OSPRayScaleArray = 'AngularVelocity'
streamTracer1Display.OSPRayScaleFunction = 'PiecewiseFunction'
streamTracer1Display.SelectOrientationVectors = 'Normals'
streamTracer1Display.ScaleFactor = 0.846682643890381
streamTracer1Display.SelectScaleArray = 'AngularVelocity'
streamTracer1Display.GlyphType = 'Arrow'
streamTracer1Display.GlyphTableIndexArray = 'AngularVelocity'
streamTracer1Display.GaussianRadius = 0.04233413219451904
streamTracer1Display.SetScaleArray = ['POINTS', 'AngularVelocity']
streamTracer1Display.ScaleTransferFunction = 'PiecewiseFunction'
streamTracer1Display.OpacityArray = ['POINTS', 'AngularVelocity']
streamTracer1Display.OpacityTransferFunction = 'PiecewiseFunction'
streamTracer1Display.DataAxesGrid = 'GridAxesRepresentation'
streamTracer1Display.PolarAxes = 'PolarAxesRepresentation'
streamTracer1Display.SelectInputVectors = ['POINTS', 'Normals']
streamTracer1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
streamTracer1Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
streamTracer1Display.ScaleTransferFunction.Points = [-0.0023003587610899603, 0.0, 0.5, 0.0, 0.0023003587419650564, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
streamTracer1Display.OpacityTransferFunction.Points = [-0.0023003587610899603, 0.0, 0.5, 0.0, 0.0023003587419650564, 1.0, 0.5, 0.0]

# show data from glyph1
glyph1Display = Show(glyph1, renderView11, 'GeometryRepresentation')

# trace defaults for the display properties.
glyph1Display.Representation = 'Surface'
glyph1Display.ColorArrayName = [None, '']
glyph1Display.Specular = 1.0
glyph1Display.SelectTCoordArray = 'None'
glyph1Display.SelectNormalArray = 'None'
glyph1Display.SelectTangentArray = 'None'
glyph1Display.EdgeColor = [0.0, 0.0, 0.0]
glyph1Display.OSPRayScaleArray = 'AngularVelocity'
glyph1Display.OSPRayScaleFunction = 'PiecewiseFunction'
glyph1Display.SelectOrientationVectors = 'Normals'
glyph1Display.ScaleFactor = 0.8376380920410157
glyph1Display.SelectScaleArray = 'AngularVelocity'
glyph1Display.GlyphType = 'Arrow'
glyph1Display.GlyphTableIndexArray = 'AngularVelocity'
glyph1Display.GaussianRadius = 0.04188190460205078
glyph1Display.SetScaleArray = ['POINTS', 'AngularVelocity']
glyph1Display.ScaleTransferFunction = 'PiecewiseFunction'
glyph1Display.OpacityArray = ['POINTS', 'AngularVelocity']
glyph1Display.OpacityTransferFunction = 'PiecewiseFunction'
glyph1Display.DataAxesGrid = 'GridAxesRepresentation'
glyph1Display.PolarAxes = 'PolarAxesRepresentation'
glyph1Display.SelectInputVectors = ['POINTS', 'Normals']
glyph1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
glyph1Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
glyph1Display.ScaleTransferFunction.Points = [-0.0020715290121826775, 0.0, 0.5, 0.0, 0.0020728366479927946, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
glyph1Display.OpacityTransferFunction.Points = [-0.0020715290121826775, 0.0, 0.5, 0.0, 0.0020728366479927946, 1.0, 0.5, 0.0]

# show data from tube4
tube4Display = Show(tube4, renderView11, 'GeometryRepresentation')

# trace defaults for the display properties.
tube4Display.Representation = 'Surface'
tube4Display.AmbientColor = [0.0, 0.12941176470588237, 0.5843137254901961]
tube4Display.ColorArrayName = ['POINTS', '']
tube4Display.DiffuseColor = [0.0, 0.12941176470588237, 0.5843137254901961]
tube4Display.Specular = 1.0
tube4Display.SelectTCoordArray = 'None'
tube4Display.SelectNormalArray = 'TubeNormals'
tube4Display.SelectTangentArray = 'None'
tube4Display.EdgeColor = [0.0, 0.0, 0.0]
tube4Display.OSPRayScaleArray = 'AngularVelocity'
tube4Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube4Display.SelectOrientationVectors = 'Normals'
tube4Display.ScaleFactor = 0.8618492603302003
tube4Display.SelectScaleArray = 'AngularVelocity'
tube4Display.GlyphType = 'Arrow'
tube4Display.GlyphTableIndexArray = 'AngularVelocity'
tube4Display.GaussianRadius = 0.04309246301651001
tube4Display.SetScaleArray = ['POINTS', 'AngularVelocity']
tube4Display.ScaleTransferFunction = 'PiecewiseFunction'
tube4Display.OpacityArray = ['POINTS', 'AngularVelocity']
tube4Display.OpacityTransferFunction = 'PiecewiseFunction'
tube4Display.DataAxesGrid = 'GridAxesRepresentation'
tube4Display.PolarAxes = 'PolarAxesRepresentation'
tube4Display.SelectInputVectors = ['POINTS', 'Normals']
tube4Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tube4Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tube4Display.ScaleTransferFunction.Points = [-0.009947089393606477, 0.0, 0.5, 0.0, 0.009942965672137077, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tube4Display.OpacityTransferFunction.Points = [-0.009947089393606477, 0.0, 0.5, 0.0, 0.009942965672137077, 1.0, 0.5, 0.0]

# show data from appendAttributes1
appendAttributes1Display = Show(appendAttributes1, renderView11, 'UniformGridRepresentation')

# trace defaults for the display properties.
appendAttributes1Display.Representation = 'Outline'
appendAttributes1Display.ColorArrayName = [None, '']
appendAttributes1Display.SelectTCoordArray = 'None'
appendAttributes1Display.SelectNormalArray = 'None'
appendAttributes1Display.SelectTangentArray = 'None'
appendAttributes1Display.OSPRayScaleArray = 'bz_jx'
appendAttributes1Display.OSPRayScaleFunction = 'PiecewiseFunction'
appendAttributes1Display.SelectOrientationVectors = 'None'
appendAttributes1Display.ScaleFactor = 1.006182531816462
appendAttributes1Display.SelectScaleArray = 'None'
appendAttributes1Display.GlyphType = 'Arrow'
appendAttributes1Display.GlyphTableIndexArray = 'None'
appendAttributes1Display.GaussianRadius = 0.050309126590823094
appendAttributes1Display.SetScaleArray = ['POINTS', 'bz_jx']
appendAttributes1Display.ScaleTransferFunction = 'PiecewiseFunction'
appendAttributes1Display.OpacityArray = ['POINTS', 'bz_jx']
appendAttributes1Display.OpacityTransferFunction = 'PiecewiseFunction'
appendAttributes1Display.DataAxesGrid = 'GridAxesRepresentation'
appendAttributes1Display.PolarAxes = 'PolarAxesRepresentation'
appendAttributes1Display.ScalarOpacityUnitDistance = 0.12315087617612483
appendAttributes1Display.OpacityArrayName = ['POINTS', 'bz_jx']
appendAttributes1Display.SliceFunction = 'Plane'
appendAttributes1Display.Slice = 63
appendAttributes1Display.SelectInputVectors = ['POINTS', 'bz_jx']
appendAttributes1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
appendAttributes1Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
appendAttributes1Display.ScaleTransferFunction.Points = [-0.4143731235557371, 0.0, 0.5, 0.0, 0.41437312355573663, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
appendAttributes1Display.OpacityTransferFunction.Points = [-0.4143731235557371, 0.0, 0.5, 0.0, 0.41437312355573663, 1.0, 0.5, 0.0]

# show data from tTKGeometrySmoother2
tTKGeometrySmoother2Display = Show(tTKGeometrySmoother2, renderView11, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
tTKGeometrySmoother2Display.Representation = 'Surface'
tTKGeometrySmoother2Display.ColorArrayName = [None, '']
tTKGeometrySmoother2Display.Specular = 1.0
tTKGeometrySmoother2Display.SelectTCoordArray = 'None'
tTKGeometrySmoother2Display.SelectNormalArray = 'None'
tTKGeometrySmoother2Display.SelectTangentArray = 'None'
tTKGeometrySmoother2Display.OSPRayScaleArray = 'oppositeOmega'
tTKGeometrySmoother2Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKGeometrySmoother2Display.SelectOrientationVectors = 'None'
tTKGeometrySmoother2Display.ScaleFactor = 0.21333734989166261
tTKGeometrySmoother2Display.SelectScaleArray = 'None'
tTKGeometrySmoother2Display.GlyphType = 'Arrow'
tTKGeometrySmoother2Display.GlyphTableIndexArray = 'None'
tTKGeometrySmoother2Display.GaussianRadius = 0.01066686749458313
tTKGeometrySmoother2Display.SetScaleArray = ['POINTS', 'oppositeOmega']
tTKGeometrySmoother2Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKGeometrySmoother2Display.OpacityArray = ['POINTS', 'oppositeOmega']
tTKGeometrySmoother2Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKGeometrySmoother2Display.DataAxesGrid = 'GridAxesRepresentation'
tTKGeometrySmoother2Display.PolarAxes = 'PolarAxesRepresentation'
tTKGeometrySmoother2Display.ScalarOpacityUnitDistance = 0.5532457135466428
tTKGeometrySmoother2Display.OpacityArrayName = ['POINTS', 'oppositeOmega']
tTKGeometrySmoother2Display.SelectInputVectors = ['POINTS', 'oppositeOmega']
tTKGeometrySmoother2Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKGeometrySmoother2Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKGeometrySmoother2Display.ScaleTransferFunction.Points = [-0.9751526647579255, 0.0, 0.5, 0.0, -0.9056711359213363, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKGeometrySmoother2Display.OpacityTransferFunction.Points = [-0.9751526647579255, 0.0, 0.5, 0.0, -0.9056711359213363, 1.0, 0.5, 0.0]

# show data from streamTracerWithCustomSource1
streamTracerWithCustomSource1Display = Show(streamTracerWithCustomSource1, renderView11, 'GeometryRepresentation')

# trace defaults for the display properties.
streamTracerWithCustomSource1Display.Representation = 'Surface'
streamTracerWithCustomSource1Display.ColorArrayName = [None, '']
streamTracerWithCustomSource1Display.Specular = 1.0
streamTracerWithCustomSource1Display.SelectTCoordArray = 'None'
streamTracerWithCustomSource1Display.SelectNormalArray = 'None'
streamTracerWithCustomSource1Display.SelectTangentArray = 'None'
streamTracerWithCustomSource1Display.EdgeColor = [0.0, 0.0, 0.0]
streamTracerWithCustomSource1Display.OSPRayScaleArray = 'AngularVelocity'
streamTracerWithCustomSource1Display.OSPRayScaleFunction = 'PiecewiseFunction'
streamTracerWithCustomSource1Display.SelectOrientationVectors = 'Normals'
streamTracerWithCustomSource1Display.ScaleFactor = 0.21557332277297975
streamTracerWithCustomSource1Display.SelectScaleArray = 'AngularVelocity'
streamTracerWithCustomSource1Display.GlyphType = 'Arrow'
streamTracerWithCustomSource1Display.GlyphTableIndexArray = 'AngularVelocity'
streamTracerWithCustomSource1Display.GaussianRadius = 0.010778666138648987
streamTracerWithCustomSource1Display.SetScaleArray = ['POINTS', 'AngularVelocity']
streamTracerWithCustomSource1Display.ScaleTransferFunction = 'PiecewiseFunction'
streamTracerWithCustomSource1Display.OpacityArray = ['POINTS', 'AngularVelocity']
streamTracerWithCustomSource1Display.OpacityTransferFunction = 'PiecewiseFunction'
streamTracerWithCustomSource1Display.DataAxesGrid = 'GridAxesRepresentation'
streamTracerWithCustomSource1Display.PolarAxes = 'PolarAxesRepresentation'
streamTracerWithCustomSource1Display.SelectInputVectors = ['POINTS', 'Normals']
streamTracerWithCustomSource1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
streamTracerWithCustomSource1Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
streamTracerWithCustomSource1Display.ScaleTransferFunction.Points = [-0.5208706210427543, 0.0, 0.5, 0.0, 0.5210735783851106, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
streamTracerWithCustomSource1Display.OpacityTransferFunction.Points = [-0.5208706210427543, 0.0, 0.5, 0.0, 0.5210735783851106, 1.0, 0.5, 0.0]

# show data from transform1
transform1Display = Show(transform1, renderView11, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
transform1Display.Representation = 'Surface'
transform1Display.ColorArrayName = [None, '']
transform1Display.Specular = 1.0
transform1Display.SelectTCoordArray = 'None'
transform1Display.SelectNormalArray = 'None'
transform1Display.SelectTangentArray = 'None'
transform1Display.OSPRayScaleArray = 'oppositeOmega'
transform1Display.OSPRayScaleFunction = 'PiecewiseFunction'
transform1Display.SelectOrientationVectors = 'None'
transform1Display.ScaleFactor = 0.21333734989166261
transform1Display.SelectScaleArray = 'None'
transform1Display.GlyphType = 'Arrow'
transform1Display.GlyphTableIndexArray = 'None'
transform1Display.GaussianRadius = 0.01066686749458313
transform1Display.SetScaleArray = ['POINTS', 'oppositeOmega']
transform1Display.ScaleTransferFunction = 'PiecewiseFunction'
transform1Display.OpacityArray = ['POINTS', 'oppositeOmega']
transform1Display.OpacityTransferFunction = 'PiecewiseFunction'
transform1Display.DataAxesGrid = 'GridAxesRepresentation'
transform1Display.PolarAxes = 'PolarAxesRepresentation'
transform1Display.ScalarOpacityUnitDistance = 0.5532457135466428
transform1Display.OpacityArrayName = ['POINTS', 'oppositeOmega']
transform1Display.SelectInputVectors = ['POINTS', 'oppositeOmega']
transform1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
transform1Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
transform1Display.ScaleTransferFunction.Points = [-0.9751526647579255, 0.0, 0.5, 0.0, -0.9056711359213363, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
transform1Display.OpacityTransferFunction.Points = [-0.9751526647579255, 0.0, 0.5, 0.0, -0.9056711359213363, 1.0, 0.5, 0.0]

# show data from tube7
tube7Display = Show(tube7, renderView11, 'GeometryRepresentation')

# trace defaults for the display properties.
tube7Display.Representation = 'Surface'
tube7Display.AmbientColor = [0.0, 0.43137254901960786, 0.0]
tube7Display.ColorArrayName = [None, '']
tube7Display.DiffuseColor = [0.0, 0.43137254901960786, 0.0]
tube7Display.Specular = 1.0
tube7Display.SelectTCoordArray = 'None'
tube7Display.SelectNormalArray = 'TubeNormals'
tube7Display.SelectTangentArray = 'None'
tube7Display.EdgeColor = [0.0, 0.0, 0.0]
tube7Display.OSPRayScaleArray = 'AngularVelocity'
tube7Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube7Display.SelectOrientationVectors = 'Normals'
tube7Display.ScaleFactor = 0.24202768802642824
tube7Display.SelectScaleArray = 'AngularVelocity'
tube7Display.GlyphType = 'Arrow'
tube7Display.GlyphTableIndexArray = 'AngularVelocity'
tube7Display.GaussianRadius = 0.012101384401321412
tube7Display.SetScaleArray = ['POINTS', 'AngularVelocity']
tube7Display.ScaleTransferFunction = 'PiecewiseFunction'
tube7Display.OpacityArray = ['POINTS', 'AngularVelocity']
tube7Display.OpacityTransferFunction = 'PiecewiseFunction'
tube7Display.DataAxesGrid = 'GridAxesRepresentation'
tube7Display.PolarAxes = 'PolarAxesRepresentation'
tube7Display.SelectInputVectors = ['POINTS', 'Normals']
tube7Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tube7Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tube7Display.ScaleTransferFunction.Points = [-0.5524262512901966, 0.0, 0.5, 0.0, 0.5525577949615347, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tube7Display.OpacityTransferFunction.Points = [-0.5524262512901966, 0.0, 0.5, 0.0, 0.5525577949615347, 1.0, 0.5, 0.0]

# show data from calculator3
calculator3Display = Show(calculator3, renderView11, 'GeometryRepresentation')

# get color transfer function/color map for 'x'
xLUT = GetColorTransferFunction('x')
xLUT.RGBPoints = [-5.03091287612915, 0.0, 0.129412, 0.584314, 4.440892098500626e-15, 0.917647, 0.941176, 0.788235, 5.03091287612915, 0.0, 0.431373, 0.0]
xLUT.ColorSpace = 'RGB'
xLUT.AboveRangeColor = [1.0, 1.0, 1.0]
xLUT.NanColor = [0.0, 0.0, 0.0]
xLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
calculator3Display.Representation = 'Surface'
calculator3Display.ColorArrayName = ['POINTS', 'x']
calculator3Display.LookupTable = xLUT
calculator3Display.Specular = 1.0
calculator3Display.SelectTCoordArray = 'None'
calculator3Display.SelectNormalArray = 'None'
calculator3Display.SelectTangentArray = 'None'
calculator3Display.EdgeColor = [0.0, 0.0, 0.0]
calculator3Display.OSPRayScaleArray = 'x'
calculator3Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator3Display.SelectOrientationVectors = 'Bz'
calculator3Display.ScaleFactor = 1.0061825752258302
calculator3Display.SelectScaleArray = 'x'
calculator3Display.GlyphType = 'Arrow'
calculator3Display.GlyphTableIndexArray = 'x'
calculator3Display.GaussianRadius = 0.050309128761291504
calculator3Display.SetScaleArray = ['POINTS', 'x']
calculator3Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator3Display.OpacityArray = ['POINTS', 'x']
calculator3Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator3Display.DataAxesGrid = 'GridAxesRepresentation'
calculator3Display.PolarAxes = 'PolarAxesRepresentation'
calculator3Display.SelectInputVectors = ['POINTS', 'Bz']
calculator3Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
calculator3Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator3Display.ScaleTransferFunction.Points = [-5.03091287612915, 0.0, 0.5, 0.0, 5.03091287612915, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator3Display.OpacityTransferFunction.Points = [-5.03091287612915, 0.0, 0.5, 0.0, 5.03091287612915, 1.0, 0.5, 0.0]

# show data from calculator4
calculator4Display = Show(calculator4, renderView11, 'GeometryRepresentation')

# get color transfer function/color map for 'y'
yLUT = GetColorTransferFunction('y')
yLUT.RGBPoints = [-4.233413219451904, 0.0, 0.129412, 0.584314, 3.552713678800501e-15, 0.917647, 0.941176, 0.788235, 4.233413219451904, 0.0, 0.431373, 0.0]
yLUT.ColorSpace = 'RGB'
yLUT.AboveRangeColor = [1.0, 1.0, 1.0]
yLUT.NanColor = [0.0, 0.0, 0.0]
yLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
calculator4Display.Representation = 'Surface'
calculator4Display.ColorArrayName = ['POINTS', 'y']
calculator4Display.LookupTable = yLUT
calculator4Display.Specular = 1.0
calculator4Display.SelectTCoordArray = 'None'
calculator4Display.SelectNormalArray = 'None'
calculator4Display.SelectTangentArray = 'None'
calculator4Display.EdgeColor = [0.0, 0.0, 0.0]
calculator4Display.OSPRayScaleArray = 'y'
calculator4Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator4Display.SelectOrientationVectors = 'Bz'
calculator4Display.ScaleFactor = 1.0061825752258302
calculator4Display.SelectScaleArray = 'y'
calculator4Display.GlyphType = 'Arrow'
calculator4Display.GlyphTableIndexArray = 'y'
calculator4Display.GaussianRadius = 0.050309128761291504
calculator4Display.SetScaleArray = ['POINTS', 'y']
calculator4Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator4Display.OpacityArray = ['POINTS', 'y']
calculator4Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator4Display.DataAxesGrid = 'GridAxesRepresentation'
calculator4Display.PolarAxes = 'PolarAxesRepresentation'
calculator4Display.SelectInputVectors = ['POINTS', 'Bz']
calculator4Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
calculator4Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator4Display.ScaleTransferFunction.Points = [-4.233413219451904, 0.0, 0.5, 0.0, 4.233413219451904, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator4Display.OpacityTransferFunction.Points = [-4.233413219451904, 0.0, 0.5, 0.0, 4.233413219451904, 1.0, 0.5, 0.0]

# show data from tTKTextureMapFromField1
tTKTextureMapFromField1Display = Show(tTKTextureMapFromField1, renderView11, 'GeometryRepresentation')

# a texture
licTextureBottom2 = CreateTexture('/data/julien/Pro/git/collaborations/gosia/tda-qchem/tda-qchem-explorations/data/LiH_MICD/png/licTextureBottom.png')

# trace defaults for the display properties.
tTKTextureMapFromField1Display.Representation = 'Surface'
tTKTextureMapFromField1Display.ColorArrayName = ['POINTS', '']
tTKTextureMapFromField1Display.Specular = 1.0
tTKTextureMapFromField1Display.SelectTCoordArray = 'UV coordinates from field'
tTKTextureMapFromField1Display.SelectNormalArray = 'None'
tTKTextureMapFromField1Display.SelectTangentArray = 'None'
tTKTextureMapFromField1Display.Texture = licTextureBottom2
tTKTextureMapFromField1Display.InterpolateTextures = 1
tTKTextureMapFromField1Display.SeamlessU = 1
tTKTextureMapFromField1Display.SeamlessV = 1
tTKTextureMapFromField1Display.EdgeColor = [0.0, 0.0, 0.0]
tTKTextureMapFromField1Display.OSPRayScaleArray = 'y'
tTKTextureMapFromField1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKTextureMapFromField1Display.SelectOrientationVectors = 'Bz'
tTKTextureMapFromField1Display.ScaleFactor = 1.0061825752258302
tTKTextureMapFromField1Display.SelectScaleArray = 'y'
tTKTextureMapFromField1Display.GlyphType = 'Arrow'
tTKTextureMapFromField1Display.GlyphTableIndexArray = 'y'
tTKTextureMapFromField1Display.GaussianRadius = 0.050309128761291504
tTKTextureMapFromField1Display.SetScaleArray = ['POINTS', 'y']
tTKTextureMapFromField1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKTextureMapFromField1Display.OpacityArray = ['POINTS', 'y']
tTKTextureMapFromField1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKTextureMapFromField1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKTextureMapFromField1Display.PolarAxes = 'PolarAxesRepresentation'
tTKTextureMapFromField1Display.SelectInputVectors = ['POINTS', 'Bz']
tTKTextureMapFromField1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKTextureMapFromField1Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKTextureMapFromField1Display.ScaleTransferFunction.Points = [-4.233413219451904, 0.0, 0.5, 0.0, 4.233413219451904, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKTextureMapFromField1Display.OpacityTransferFunction.Points = [-4.233413219451904, 0.0, 0.5, 0.0, 4.233413219451904, 1.0, 0.5, 0.0]

# show data from streamTracer2
streamTracer2Display = Show(streamTracer2, renderView11, 'GeometryRepresentation')

# trace defaults for the display properties.
streamTracer2Display.Representation = 'Surface'
streamTracer2Display.ColorArrayName = ['POINTS', 'Bz']
streamTracer2Display.LookupTable = bzLUT
streamTracer2Display.Specular = 1.0
streamTracer2Display.SelectTCoordArray = 'None'
streamTracer2Display.SelectNormalArray = 'None'
streamTracer2Display.SelectTangentArray = 'None'
streamTracer2Display.EdgeColor = [0.0, 0.0, 0.0]
streamTracer2Display.OSPRayScaleArray = 'AngularVelocity'
streamTracer2Display.OSPRayScaleFunction = 'PiecewiseFunction'
streamTracer2Display.SelectOrientationVectors = 'Normals'
streamTracer2Display.ScaleFactor = 0.8469868659973145
streamTracer2Display.SelectScaleArray = 'AngularVelocity'
streamTracer2Display.GlyphType = 'Arrow'
streamTracer2Display.GlyphTableIndexArray = 'AngularVelocity'
streamTracer2Display.GaussianRadius = 0.04234934329986572
streamTracer2Display.SetScaleArray = ['POINTS', 'AngularVelocity']
streamTracer2Display.ScaleTransferFunction = 'PiecewiseFunction'
streamTracer2Display.OpacityArray = ['POINTS', 'AngularVelocity']
streamTracer2Display.OpacityTransferFunction = 'PiecewiseFunction'
streamTracer2Display.DataAxesGrid = 'GridAxesRepresentation'
streamTracer2Display.PolarAxes = 'PolarAxesRepresentation'
streamTracer2Display.SelectInputVectors = ['POINTS', 'Normals']
streamTracer2Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
streamTracer2Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
streamTracer2Display.ScaleTransferFunction.Points = [-0.002435294164725561, 0.0, 0.5, 0.0, 0.0024269388090187734, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
streamTracer2Display.OpacityTransferFunction.Points = [-0.002435294164725561, 0.0, 0.5, 0.0, 0.0024269388090187734, 1.0, 0.5, 0.0]

# show data from tube5
tube5Display = Show(tube5, renderView11, 'GeometryRepresentation')

# trace defaults for the display properties.
tube5Display.Representation = 'Surface'
tube5Display.AmbientColor = [0.0, 0.12941176470588237, 0.5843137254901961]
tube5Display.ColorArrayName = ['POINTS', '']
tube5Display.DiffuseColor = [0.0, 0.12941176470588237, 0.5843137254901961]
tube5Display.Specular = 1.0
tube5Display.SelectTCoordArray = 'None'
tube5Display.SelectNormalArray = 'TubeNormals'
tube5Display.SelectTangentArray = 'None'
tube5Display.EdgeColor = [0.0, 0.0, 0.0]
tube5Display.OSPRayScaleArray = 'AngularVelocity'
tube5Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube5Display.SelectOrientationVectors = 'Normals'
tube5Display.ScaleFactor = 0.8619880199432374
tube5Display.SelectScaleArray = 'AngularVelocity'
tube5Display.GlyphType = 'Arrow'
tube5Display.GlyphTableIndexArray = 'AngularVelocity'
tube5Display.GaussianRadius = 0.04309940099716186
tube5Display.SetScaleArray = ['POINTS', 'AngularVelocity']
tube5Display.ScaleTransferFunction = 'PiecewiseFunction'
tube5Display.OpacityArray = ['POINTS', 'AngularVelocity']
tube5Display.OpacityTransferFunction = 'PiecewiseFunction'
tube5Display.DataAxesGrid = 'GridAxesRepresentation'
tube5Display.PolarAxes = 'PolarAxesRepresentation'
tube5Display.SelectInputVectors = ['POINTS', 'Normals']
tube5Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tube5Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tube5Display.ScaleTransferFunction.Points = [-0.002274907936430137, 0.0, 0.5, 0.0, 0.0023252478649755754, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tube5Display.OpacityTransferFunction.Points = [-0.002274907936430137, 0.0, 0.5, 0.0, 0.0023252478649755754, 1.0, 0.5, 0.0]

# show data from transform2
transform2Display = Show(transform2, renderView11, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
transform2Display.Representation = 'Surface'
transform2Display.AmbientColor = [0.6666666666666666, 0.21176470588235294, 0.19607843137254902]
transform2Display.ColorArrayName = [None, '']
transform2Display.DiffuseColor = [0.6666666666666666, 0.21176470588235294, 0.19607843137254902]
transform2Display.Specular = 1.0
transform2Display.SelectTCoordArray = 'None'
transform2Display.SelectNormalArray = 'None'
transform2Display.SelectTangentArray = 'None'
transform2Display.OSPRayScaleArray = 'oppositeOmega'
transform2Display.OSPRayScaleFunction = 'PiecewiseFunction'
transform2Display.SelectOrientationVectors = 'None'
transform2Display.ScaleFactor = 0.5546771049499511
transform2Display.SelectScaleArray = 'None'
transform2Display.GlyphType = 'Arrow'
transform2Display.GlyphTableIndexArray = 'None'
transform2Display.GaussianRadius = 0.02773385524749756
transform2Display.SetScaleArray = ['POINTS', 'oppositeOmega']
transform2Display.ScaleTransferFunction = 'PiecewiseFunction'
transform2Display.OpacityArray = ['POINTS', 'oppositeOmega']
transform2Display.OpacityTransferFunction = 'PiecewiseFunction'
transform2Display.DataAxesGrid = 'GridAxesRepresentation'
transform2Display.PolarAxes = 'PolarAxesRepresentation'
transform2Display.ScalarOpacityUnitDistance = 1.4384388475814798
transform2Display.OpacityArrayName = ['POINTS', 'oppositeOmega']
transform2Display.SelectInputVectors = ['POINTS', 'oppositeOmega']
transform2Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
transform2Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
transform2Display.ScaleTransferFunction.Points = [-0.9751526647579255, 0.0, 0.5, 0.0, -0.9056711359213363, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
transform2Display.OpacityTransferFunction.Points = [-0.9751526647579255, 0.0, 0.5, 0.0, -0.9056711359213363, 1.0, 0.5, 0.0]

# show data from streamTracerWithCustomSource2
streamTracerWithCustomSource2Display = Show(streamTracerWithCustomSource2, renderView11, 'GeometryRepresentation')

# trace defaults for the display properties.
streamTracerWithCustomSource2Display.Representation = 'Surface'
streamTracerWithCustomSource2Display.ColorArrayName = ['POINTS', 'Bz']
streamTracerWithCustomSource2Display.LookupTable = bzLUT
streamTracerWithCustomSource2Display.Specular = 1.0
streamTracerWithCustomSource2Display.SelectTCoordArray = 'None'
streamTracerWithCustomSource2Display.SelectNormalArray = 'None'
streamTracerWithCustomSource2Display.SelectTangentArray = 'None'
streamTracerWithCustomSource2Display.EdgeColor = [0.0, 0.0, 0.0]
streamTracerWithCustomSource2Display.OSPRayScaleArray = 'AngularVelocity'
streamTracerWithCustomSource2Display.OSPRayScaleFunction = 'PiecewiseFunction'
streamTracerWithCustomSource2Display.SelectOrientationVectors = 'Normals'
streamTracerWithCustomSource2Display.ScaleFactor = 0.8468880653381348
streamTracerWithCustomSource2Display.SelectScaleArray = 'AngularVelocity'
streamTracerWithCustomSource2Display.GlyphType = 'Arrow'
streamTracerWithCustomSource2Display.GlyphTableIndexArray = 'AngularVelocity'
streamTracerWithCustomSource2Display.GaussianRadius = 0.04234440326690674
streamTracerWithCustomSource2Display.SetScaleArray = ['POINTS', 'AngularVelocity']
streamTracerWithCustomSource2Display.ScaleTransferFunction = 'PiecewiseFunction'
streamTracerWithCustomSource2Display.OpacityArray = ['POINTS', 'AngularVelocity']
streamTracerWithCustomSource2Display.OpacityTransferFunction = 'PiecewiseFunction'
streamTracerWithCustomSource2Display.DataAxesGrid = 'GridAxesRepresentation'
streamTracerWithCustomSource2Display.PolarAxes = 'PolarAxesRepresentation'
streamTracerWithCustomSource2Display.SelectInputVectors = ['POINTS', 'Normals']
streamTracerWithCustomSource2Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
streamTracerWithCustomSource2Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
streamTracerWithCustomSource2Display.ScaleTransferFunction.Points = [-0.04157313645200568, 0.0, 0.5, 0.0, 0.04161219663310649, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
streamTracerWithCustomSource2Display.OpacityTransferFunction.Points = [-0.04157313645200568, 0.0, 0.5, 0.0, 0.04161219663310649, 1.0, 0.5, 0.0]

# show data from tube6
tube6Display = Show(tube6, renderView11, 'GeometryRepresentation')

# trace defaults for the display properties.
tube6Display.Representation = 'Surface'
tube6Display.AmbientColor = [0.0, 0.43137254901960786, 0.0]
tube6Display.ColorArrayName = ['POINTS', '']
tube6Display.DiffuseColor = [0.0, 0.43137254901960786, 0.0]
tube6Display.Specular = 1.0
tube6Display.SelectTCoordArray = 'None'
tube6Display.SelectNormalArray = 'TubeNormals'
tube6Display.SelectTangentArray = 'None'
tube6Display.EdgeColor = [0.0, 0.0, 0.0]
tube6Display.OSPRayScaleArray = 'AngularVelocity'
tube6Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube6Display.SelectOrientationVectors = 'Normals'
tube6Display.ScaleFactor = 0.8580793380737305
tube6Display.SelectScaleArray = 'AngularVelocity'
tube6Display.GlyphType = 'Arrow'
tube6Display.GlyphTableIndexArray = 'AngularVelocity'
tube6Display.GaussianRadius = 0.04290396690368652
tube6Display.SetScaleArray = ['POINTS', 'AngularVelocity']
tube6Display.ScaleTransferFunction = 'PiecewiseFunction'
tube6Display.OpacityArray = ['POINTS', 'AngularVelocity']
tube6Display.OpacityTransferFunction = 'PiecewiseFunction'
tube6Display.DataAxesGrid = 'GridAxesRepresentation'
tube6Display.PolarAxes = 'PolarAxesRepresentation'
tube6Display.SelectInputVectors = ['POINTS', 'Normals']
tube6Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tube6Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tube6Display.ScaleTransferFunction.Points = [-0.047227937488971354, 0.0, 0.5, 0.0, 0.047227942494882026, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tube6Display.OpacityTransferFunction.Points = [-0.047227937488971354, 0.0, 0.5, 0.0, 0.047227942494882026, 1.0, 0.5, 0.0]

# show data from slice2
slice2Display = Show(slice2, renderView11, 'GeometryRepresentation')

# trace defaults for the display properties.
slice2Display.Representation = 'Surface LIC'
slice2Display.ColorArrayName = ['POINTS', 'Bz']
slice2Display.LookupTable = bzLUT
slice2Display.Specular = 1.0
slice2Display.SelectTCoordArray = 'None'
slice2Display.SelectNormalArray = 'None'
slice2Display.SelectTangentArray = 'None'
slice2Display.EdgeColor = [0.0, 0.0, 0.0]
slice2Display.OSPRayScaleArray = 'Bz'
slice2Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice2Display.SelectOrientationVectors = 'Bz'
slice2Display.ScaleFactor = 0.846682643890381
slice2Display.SelectScaleArray = 'Bz'
slice2Display.GlyphType = 'Arrow'
slice2Display.GlyphTableIndexArray = 'Bz'
slice2Display.GaussianRadius = 0.04233413219451904
slice2Display.SetScaleArray = ['POINTS', 'Bz']
slice2Display.ScaleTransferFunction = 'PiecewiseFunction'
slice2Display.OpacityArray = ['POINTS', 'Bz']
slice2Display.OpacityTransferFunction = 'PiecewiseFunction'
slice2Display.DataAxesGrid = 'GridAxesRepresentation'
slice2Display.PolarAxes = 'PolarAxesRepresentation'
slice2Display.SelectInputVectors = ['POINTS', 'Bz']
slice2Display.LICIntensity = 0.6
slice2Display.EnhanceContrast = 'LIC and Color'
slice2Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
slice2Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice2Display.ScaleTransferFunction.Points = [-0.0008344839921660763, 0.0, 0.5, 0.0, 0.0008344839921660763, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice2Display.OpacityTransferFunction.Points = [-0.0008344839921660763, 0.0, 0.5, 0.0, 0.0008344839921660763, 1.0, 0.5, 0.0]

# show data from calculator5
calculator5Display = Show(calculator5, renderView11, 'GeometryRepresentation')

# trace defaults for the display properties.
calculator5Display.Representation = 'Surface'
calculator5Display.ColorArrayName = ['POINTS', 'x']
calculator5Display.LookupTable = xLUT
calculator5Display.Specular = 1.0
calculator5Display.SelectTCoordArray = 'None'
calculator5Display.SelectNormalArray = 'None'
calculator5Display.SelectTangentArray = 'None'
calculator5Display.EdgeColor = [0.0, 0.0, 0.0]
calculator5Display.OSPRayScaleArray = 'x'
calculator5Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator5Display.SelectOrientationVectors = 'Bz'
calculator5Display.ScaleFactor = 0.846682643890381
calculator5Display.SelectScaleArray = 'x'
calculator5Display.GlyphType = 'Arrow'
calculator5Display.GlyphTableIndexArray = 'x'
calculator5Display.GaussianRadius = 0.04233413219451904
calculator5Display.SetScaleArray = ['POINTS', 'x']
calculator5Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator5Display.OpacityArray = ['POINTS', 'x']
calculator5Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator5Display.DataAxesGrid = 'GridAxesRepresentation'
calculator5Display.PolarAxes = 'PolarAxesRepresentation'
calculator5Display.SelectInputVectors = ['POINTS', 'Bz']
calculator5Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
calculator5Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator5Display.ScaleTransferFunction.Points = [4.044891357421875, 0.0, 0.5, 0.0, 4.045867919921875, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator5Display.OpacityTransferFunction.Points = [4.044891357421875, 0.0, 0.5, 0.0, 4.045867919921875, 1.0, 0.5, 0.0]

# show data from calculator6
calculator6Display = Show(calculator6, renderView11, 'GeometryRepresentation')

# trace defaults for the display properties.
calculator6Display.Representation = 'Surface'
calculator6Display.ColorArrayName = ['POINTS', 'y']
calculator6Display.LookupTable = yLUT
calculator6Display.Specular = 1.0
calculator6Display.SelectTCoordArray = 'None'
calculator6Display.SelectNormalArray = 'None'
calculator6Display.SelectTangentArray = 'None'
calculator6Display.EdgeColor = [0.0, 0.0, 0.0]
calculator6Display.OSPRayScaleArray = 'y'
calculator6Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator6Display.SelectOrientationVectors = 'Bz'
calculator6Display.ScaleFactor = 0.846682643890381
calculator6Display.SelectScaleArray = 'y'
calculator6Display.GlyphType = 'Arrow'
calculator6Display.GlyphTableIndexArray = 'y'
calculator6Display.GaussianRadius = 0.04233413219451904
calculator6Display.SetScaleArray = ['POINTS', 'y']
calculator6Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator6Display.OpacityArray = ['POINTS', 'y']
calculator6Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator6Display.DataAxesGrid = 'GridAxesRepresentation'
calculator6Display.PolarAxes = 'PolarAxesRepresentation'
calculator6Display.SelectInputVectors = ['POINTS', 'Bz']
calculator6Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
calculator6Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator6Display.ScaleTransferFunction.Points = [-4.233413219451904, 0.0, 0.5, 0.0, 4.233413219451904, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator6Display.OpacityTransferFunction.Points = [-4.233413219451904, 0.0, 0.5, 0.0, 4.233413219451904, 1.0, 0.5, 0.0]

# show data from tTKTextureMapFromField2
tTKTextureMapFromField2Display = Show(tTKTextureMapFromField2, renderView11, 'GeometryRepresentation')

# a texture
licTextureSide2 = CreateTexture('/data/julien/Pro/git/collaborations/gosia/tda-qchem/tda-qchem-explorations/data/LiH_MICD/png/licTextureSide.png')

# trace defaults for the display properties.
tTKTextureMapFromField2Display.Representation = 'Surface'
tTKTextureMapFromField2Display.ColorArrayName = ['POINTS', '']
tTKTextureMapFromField2Display.Specular = 1.0
tTKTextureMapFromField2Display.SelectTCoordArray = 'UV coordinates from field'
tTKTextureMapFromField2Display.SelectNormalArray = 'None'
tTKTextureMapFromField2Display.SelectTangentArray = 'None'
tTKTextureMapFromField2Display.Texture = licTextureSide2
tTKTextureMapFromField2Display.InterpolateTextures = 1
tTKTextureMapFromField2Display.SeamlessU = 1
tTKTextureMapFromField2Display.SeamlessV = 1
tTKTextureMapFromField2Display.EdgeColor = [0.0, 0.0, 0.0]
tTKTextureMapFromField2Display.OSPRayScaleArray = 'y'
tTKTextureMapFromField2Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKTextureMapFromField2Display.SelectOrientationVectors = 'Bz'
tTKTextureMapFromField2Display.ScaleFactor = 0.846682643890381
tTKTextureMapFromField2Display.SelectScaleArray = 'y'
tTKTextureMapFromField2Display.GlyphType = 'Arrow'
tTKTextureMapFromField2Display.GlyphTableIndexArray = 'y'
tTKTextureMapFromField2Display.GaussianRadius = 0.04233413219451904
tTKTextureMapFromField2Display.SetScaleArray = ['POINTS', 'y']
tTKTextureMapFromField2Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKTextureMapFromField2Display.OpacityArray = ['POINTS', 'y']
tTKTextureMapFromField2Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKTextureMapFromField2Display.DataAxesGrid = 'GridAxesRepresentation'
tTKTextureMapFromField2Display.PolarAxes = 'PolarAxesRepresentation'
tTKTextureMapFromField2Display.SelectInputVectors = ['POINTS', 'Bz']
tTKTextureMapFromField2Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKTextureMapFromField2Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKTextureMapFromField2Display.ScaleTransferFunction.Points = [-4.233413219451904, 0.0, 0.5, 0.0, 4.233413219451904, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKTextureMapFromField2Display.OpacityTransferFunction.Points = [-4.233413219451904, 0.0, 0.5, 0.0, 4.233413219451904, 1.0, 0.5, 0.0]

# show data from slice3
slice3Display = Show(slice3, renderView11, 'GeometryRepresentation')

# trace defaults for the display properties.
slice3Display.Representation = 'Surface LIC'
slice3Display.ColorArrayName = ['POINTS', 'Bz']
slice3Display.LookupTable = bzLUT
slice3Display.Specular = 1.0
slice3Display.SelectTCoordArray = 'None'
slice3Display.SelectNormalArray = 'None'
slice3Display.SelectTangentArray = 'None'
slice3Display.EdgeColor = [0.0, 0.0, 0.0]
slice3Display.OSPRayScaleArray = 'Bz'
slice3Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice3Display.SelectOrientationVectors = 'Bz'
slice3Display.ScaleFactor = 1.0061825752258302
slice3Display.SelectScaleArray = 'Bz'
slice3Display.GlyphType = 'Arrow'
slice3Display.GlyphTableIndexArray = 'Bz'
slice3Display.GaussianRadius = 0.050309128761291504
slice3Display.SetScaleArray = ['POINTS', 'Bz']
slice3Display.ScaleTransferFunction = 'PiecewiseFunction'
slice3Display.OpacityArray = ['POINTS', 'Bz']
slice3Display.OpacityTransferFunction = 'PiecewiseFunction'
slice3Display.DataAxesGrid = 'GridAxesRepresentation'
slice3Display.PolarAxes = 'PolarAxesRepresentation'
slice3Display.SelectInputVectors = ['POINTS', 'Bz']
slice3Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
slice3Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice3Display.ScaleTransferFunction.Points = [-0.00010881522166928599, 0.0, 0.5, 0.0, 0.00368209482938846, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice3Display.OpacityTransferFunction.Points = [-0.00010881522166928599, 0.0, 0.5, 0.0, 0.00368209482938846, 1.0, 0.5, 0.0]

# show data from calculator7
calculator7Display = Show(calculator7, renderView11, 'GeometryRepresentation')

# get color transfer function/color map for 'u'
uLUT = GetColorTransferFunction('u')
uLUT.RGBPoints = [-5.03091287612915, 0.0, 0.129412, 0.584314, 4.440892098500626e-15, 0.917647, 0.941176, 0.788235, 5.03091287612915, 0.0, 0.431373, 0.0]
uLUT.ColorSpace = 'RGB'
uLUT.AboveRangeColor = [1.0, 1.0, 1.0]
uLUT.NanColor = [0.0, 0.0, 0.0]
uLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
calculator7Display.Representation = 'Surface'
calculator7Display.ColorArrayName = ['POINTS', 'u']
calculator7Display.LookupTable = uLUT
calculator7Display.Specular = 1.0
calculator7Display.SelectTCoordArray = 'None'
calculator7Display.SelectNormalArray = 'None'
calculator7Display.SelectTangentArray = 'None'
calculator7Display.EdgeColor = [0.0, 0.0, 0.0]
calculator7Display.OSPRayScaleArray = 'u'
calculator7Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator7Display.SelectOrientationVectors = 'Bz'
calculator7Display.ScaleFactor = 1.0061825752258302
calculator7Display.SelectScaleArray = 'u'
calculator7Display.GlyphType = 'Arrow'
calculator7Display.GlyphTableIndexArray = 'u'
calculator7Display.GaussianRadius = 0.050309128761291504
calculator7Display.SetScaleArray = ['POINTS', 'u']
calculator7Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator7Display.OpacityArray = ['POINTS', 'u']
calculator7Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator7Display.DataAxesGrid = 'GridAxesRepresentation'
calculator7Display.PolarAxes = 'PolarAxesRepresentation'
calculator7Display.SelectInputVectors = ['POINTS', 'Bz']
calculator7Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
calculator7Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator7Display.ScaleTransferFunction.Points = [-5.03091287612915, 0.0, 0.5, 0.0, 5.03091287612915, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator7Display.OpacityTransferFunction.Points = [-5.03091287612915, 0.0, 0.5, 0.0, 5.03091287612915, 1.0, 0.5, 0.0]

# show data from calculator8
calculator8Display = Show(calculator8, renderView11, 'GeometryRepresentation')

# get color transfer function/color map for 'v'
vLUT = GetColorTransferFunction('v')
vLUT.RGBPoints = [-4.233413219451904, 0.0, 0.129412, 0.584314, 3.552713678800501e-15, 0.917647, 0.941176, 0.788235, 4.233413219451904, 0.0, 0.431373, 0.0]
vLUT.ColorSpace = 'RGB'
vLUT.AboveRangeColor = [1.0, 1.0, 1.0]
vLUT.NanColor = [0.0, 0.0, 0.0]
vLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
calculator8Display.Representation = 'Surface'
calculator8Display.ColorArrayName = ['POINTS', 'v']
calculator8Display.LookupTable = vLUT
calculator8Display.Specular = 1.0
calculator8Display.SelectTCoordArray = 'None'
calculator8Display.SelectNormalArray = 'None'
calculator8Display.SelectTangentArray = 'None'
calculator8Display.EdgeColor = [0.0, 0.0, 0.0]
calculator8Display.OSPRayScaleArray = 'v'
calculator8Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator8Display.SelectOrientationVectors = 'Bz'
calculator8Display.ScaleFactor = 1.0061825752258302
calculator8Display.SelectScaleArray = 'v'
calculator8Display.GlyphType = 'Arrow'
calculator8Display.GlyphTableIndexArray = 'v'
calculator8Display.GaussianRadius = 0.050309128761291504
calculator8Display.SetScaleArray = ['POINTS', 'v']
calculator8Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator8Display.OpacityArray = ['POINTS', 'v']
calculator8Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator8Display.DataAxesGrid = 'GridAxesRepresentation'
calculator8Display.PolarAxes = 'PolarAxesRepresentation'
calculator8Display.SelectInputVectors = ['POINTS', 'Bz']
calculator8Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
calculator8Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator8Display.ScaleTransferFunction.Points = [-4.233413219451904, 0.0, 0.5, 0.0, 4.233413219451904, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator8Display.OpacityTransferFunction.Points = [-4.233413219451904, 0.0, 0.5, 0.0, 4.233413219451904, 1.0, 0.5, 0.0]

# show data from tTKTextureMapFromField3
tTKTextureMapFromField3Display = Show(tTKTextureMapFromField3, renderView11, 'GeometryRepresentation')

# a texture
licTextureBack2 = CreateTexture('/data/julien/Pro/git/collaborations/gosia/tda-qchem/tda-qchem-explorations/data/LiH_MICD/png/licTextureBack.png')

# trace defaults for the display properties.
tTKTextureMapFromField3Display.Representation = 'Surface'
tTKTextureMapFromField3Display.ColorArrayName = ['POINTS', '']
tTKTextureMapFromField3Display.Specular = 1.0
tTKTextureMapFromField3Display.SelectTCoordArray = 'UV coordinates from field'
tTKTextureMapFromField3Display.SelectNormalArray = 'None'
tTKTextureMapFromField3Display.SelectTangentArray = 'None'
tTKTextureMapFromField3Display.Texture = licTextureBack2
tTKTextureMapFromField3Display.EdgeColor = [0.0, 0.0, 0.0]
tTKTextureMapFromField3Display.OSPRayScaleArray = 'v'
tTKTextureMapFromField3Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKTextureMapFromField3Display.SelectOrientationVectors = 'Bz'
tTKTextureMapFromField3Display.ScaleFactor = 1.0061825752258302
tTKTextureMapFromField3Display.SelectScaleArray = 'v'
tTKTextureMapFromField3Display.GlyphType = 'Arrow'
tTKTextureMapFromField3Display.GlyphTableIndexArray = 'v'
tTKTextureMapFromField3Display.GaussianRadius = 0.050309128761291504
tTKTextureMapFromField3Display.SetScaleArray = ['POINTS', 'v']
tTKTextureMapFromField3Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKTextureMapFromField3Display.OpacityArray = ['POINTS', 'v']
tTKTextureMapFromField3Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKTextureMapFromField3Display.DataAxesGrid = 'GridAxesRepresentation'
tTKTextureMapFromField3Display.PolarAxes = 'PolarAxesRepresentation'
tTKTextureMapFromField3Display.SelectInputVectors = ['POINTS', 'Bz']
tTKTextureMapFromField3Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKTextureMapFromField3Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKTextureMapFromField3Display.ScaleTransferFunction.Points = [-4.233413219451904, 0.0, 0.5, 0.0, 4.233413219451904, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKTextureMapFromField3Display.OpacityTransferFunction.Points = [-4.233413219451904, 0.0, 0.5, 0.0, 4.233413219451904, 1.0, 0.5, 0.0]

# hide data in view
Hide(start_data_bzvti, renderView11)

# hide data in view
Hide(calculator2, renderView11)

# hide data in view
Hide(slice1, renderView11)

# hide data in view
Hide(contour1, renderView11)

# hide data in view
Hide(streamTracer1, renderView11)

# hide data in view
Hide(glyph1, renderView11)

# hide data in view
Hide(appendAttributes1, renderView11)

# hide data in view
Hide(tTKGeometrySmoother2, renderView11)

# hide data in view
Hide(streamTracerWithCustomSource1, renderView11)

# hide data in view
Hide(transform1, renderView11)

# hide data in view
Hide(calculator3, renderView11)

# hide data in view
Hide(calculator4, renderView11)

# hide data in view
Hide(streamTracer2, renderView11)

# hide data in view
Hide(transform2, renderView11)

# hide data in view
Hide(streamTracerWithCustomSource2, renderView11)

# hide data in view
Hide(slice2, renderView11)

# hide data in view
Hide(calculator5, renderView11)

# hide data in view
Hide(calculator6, renderView11)

# hide data in view
Hide(slice3, renderView11)

# hide data in view
Hide(calculator7, renderView11)

# hide data in view
Hide(calculator8, renderView11)

# ----------------------------------------------------------------
# setup the visualization in view 'renderView12'
# ----------------------------------------------------------------

# show data from slice1
slice1Display_1 = Show(slice1, renderView12, 'GeometryRepresentation')

# trace defaults for the display properties.
slice1Display_1.Representation = 'Surface LIC'
slice1Display_1.ColorArrayName = ['POINTS', 'Bz']
slice1Display_1.LookupTable = bzLUT
slice1Display_1.Specular = 1.0
slice1Display_1.SelectTCoordArray = 'None'
slice1Display_1.SelectNormalArray = 'None'
slice1Display_1.SelectTangentArray = 'None'
slice1Display_1.EdgeColor = [0.0, 0.0, 0.0]
slice1Display_1.OSPRayScaleArray = 'Bz'
slice1Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
slice1Display_1.SelectOrientationVectors = 'Bz'
slice1Display_1.ScaleFactor = 1.0061825752258302
slice1Display_1.SelectScaleArray = 'Bz'
slice1Display_1.GlyphType = 'Arrow'
slice1Display_1.GlyphTableIndexArray = 'Bz'
slice1Display_1.GaussianRadius = 0.050309128761291504
slice1Display_1.SetScaleArray = ['POINTS', 'Bz']
slice1Display_1.ScaleTransferFunction = 'PiecewiseFunction'
slice1Display_1.OpacityArray = ['POINTS', 'Bz']
slice1Display_1.OpacityTransferFunction = 'PiecewiseFunction'
slice1Display_1.DataAxesGrid = 'GridAxesRepresentation'
slice1Display_1.PolarAxes = 'PolarAxesRepresentation'
slice1Display_1.SelectInputVectors = ['POINTS', 'Bz']
slice1Display_1.LICIntensity = 0.6
slice1Display_1.EnhanceContrast = 'LIC and Color'
slice1Display_1.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
slice1Display_1.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice1Display_1.ScaleTransferFunction.Points = [-0.4143731230557486, 0.0, 0.5, 0.0, 0.41437312305574814, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice1Display_1.OpacityTransferFunction.Points = [-0.4143731230557486, 0.0, 0.5, 0.0, 0.41437312305574814, 1.0, 0.5, 0.0]

# ----------------------------------------------------------------
# setup the visualization in view 'renderView13'
# ----------------------------------------------------------------

# show data from slice2
slice2Display_1 = Show(slice2, renderView13, 'GeometryRepresentation')

# trace defaults for the display properties.
slice2Display_1.Representation = 'Surface LIC'
slice2Display_1.ColorArrayName = ['POINTS', 'Bz']
slice2Display_1.LookupTable = bzLUT
slice2Display_1.Specular = 1.0
slice2Display_1.SelectTCoordArray = 'None'
slice2Display_1.SelectNormalArray = 'None'
slice2Display_1.SelectTangentArray = 'None'
slice2Display_1.EdgeColor = [0.0, 0.0, 0.0]
slice2Display_1.OSPRayScaleArray = 'Bz'
slice2Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
slice2Display_1.SelectOrientationVectors = 'Bz'
slice2Display_1.ScaleFactor = 0.846682643890381
slice2Display_1.SelectScaleArray = 'Bz'
slice2Display_1.GlyphType = 'Arrow'
slice2Display_1.GlyphTableIndexArray = 'Bz'
slice2Display_1.GaussianRadius = 0.04233413219451904
slice2Display_1.SetScaleArray = ['POINTS', 'Bz']
slice2Display_1.ScaleTransferFunction = 'PiecewiseFunction'
slice2Display_1.OpacityArray = ['POINTS', 'Bz']
slice2Display_1.OpacityTransferFunction = 'PiecewiseFunction'
slice2Display_1.DataAxesGrid = 'GridAxesRepresentation'
slice2Display_1.PolarAxes = 'PolarAxesRepresentation'
slice2Display_1.SelectInputVectors = ['POINTS', 'Bz']
slice2Display_1.LICIntensity = 0.6
slice2Display_1.EnhanceContrast = 'LIC and Color'
slice2Display_1.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
slice2Display_1.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice2Display_1.ScaleTransferFunction.Points = [-0.00042519138157758436, 0.0, 0.5, 0.0, 0.0004251913815775849, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice2Display_1.OpacityTransferFunction.Points = [-0.00042519138157758436, 0.0, 0.5, 0.0, 0.0004251913815775849, 1.0, 0.5, 0.0]

# ----------------------------------------------------------------
# setup the visualization in view 'renderView14'
# ----------------------------------------------------------------

# show data from slice3
slice3Display_1 = Show(slice3, renderView14, 'GeometryRepresentation')

# trace defaults for the display properties.
slice3Display_1.Representation = 'Surface LIC'
slice3Display_1.ColorArrayName = ['POINTS', 'Bz']
slice3Display_1.LookupTable = bzLUT
slice3Display_1.Specular = 1.0
slice3Display_1.SelectTCoordArray = 'None'
slice3Display_1.SelectNormalArray = 'None'
slice3Display_1.SelectTangentArray = 'None'
slice3Display_1.EdgeColor = [0.0, 0.0, 0.0]
slice3Display_1.OSPRayScaleArray = 'Bz'
slice3Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
slice3Display_1.SelectOrientationVectors = 'Bz'
slice3Display_1.ScaleFactor = 1.0061825752258302
slice3Display_1.SelectScaleArray = 'Bz'
slice3Display_1.GlyphType = 'Arrow'
slice3Display_1.GlyphTableIndexArray = 'Bz'
slice3Display_1.GaussianRadius = 0.050309128761291504
slice3Display_1.SetScaleArray = ['POINTS', 'Bz']
slice3Display_1.ScaleTransferFunction = 'PiecewiseFunction'
slice3Display_1.OpacityArray = ['POINTS', 'Bz']
slice3Display_1.OpacityTransferFunction = 'PiecewiseFunction'
slice3Display_1.DataAxesGrid = 'GridAxesRepresentation'
slice3Display_1.PolarAxes = 'PolarAxesRepresentation'
slice3Display_1.SelectInputVectors = ['POINTS', 'Bz']
slice3Display_1.LICIntensity = 0.6
slice3Display_1.EnhanceContrast = 'LIC and Color'
slice3Display_1.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
slice3Display_1.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice3Display_1.ScaleTransferFunction.Points = [-0.00010881522166928599, 0.0, 0.5, 0.0, 0.00368209482938846, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice3Display_1.OpacityTransferFunction.Points = [-0.00010881522166928599, 0.0, 0.5, 0.0, 0.00368209482938846, 1.0, 0.5, 0.0]

# ----------------------------------------------------------------
# setup the visualization in view 'renderView2'
# ----------------------------------------------------------------

# show data from start_data_omega_bzvti
start_data_omega_bzvtiDisplay_2 = Show(start_data_omega_bzvti, renderView2, 'UniformGridRepresentation')

# trace defaults for the display properties.
start_data_omega_bzvtiDisplay_2.Representation = 'Outline'
start_data_omega_bzvtiDisplay_2.AmbientColor = [0.1803921568627451, 0.17647058823529413, 0.17647058823529413]
start_data_omega_bzvtiDisplay_2.ColorArrayName = ['POINTS', '']
start_data_omega_bzvtiDisplay_2.DiffuseColor = [0.1803921568627451, 0.17647058823529413, 0.17647058823529413]
start_data_omega_bzvtiDisplay_2.SelectTCoordArray = 'None'
start_data_omega_bzvtiDisplay_2.SelectNormalArray = 'None'
start_data_omega_bzvtiDisplay_2.SelectTangentArray = 'None'
start_data_omega_bzvtiDisplay_2.OSPRayScaleArray = 'bz_wz'
start_data_omega_bzvtiDisplay_2.OSPRayScaleFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay_2.SelectOrientationVectors = 'None'
start_data_omega_bzvtiDisplay_2.ScaleFactor = 1.006182531816462
start_data_omega_bzvtiDisplay_2.SelectScaleArray = 'None'
start_data_omega_bzvtiDisplay_2.GlyphType = 'Arrow'
start_data_omega_bzvtiDisplay_2.GlyphTableIndexArray = 'None'
start_data_omega_bzvtiDisplay_2.GaussianRadius = 0.050309126590823094
start_data_omega_bzvtiDisplay_2.SetScaleArray = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_2.ScaleTransferFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay_2.OpacityArray = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_2.OpacityTransferFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay_2.DataAxesGrid = 'GridAxesRepresentation'
start_data_omega_bzvtiDisplay_2.PolarAxes = 'PolarAxesRepresentation'
start_data_omega_bzvtiDisplay_2.ScalarOpacityUnitDistance = 0.12315087617612483
start_data_omega_bzvtiDisplay_2.OpacityArrayName = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_2.SliceFunction = 'Plane'
start_data_omega_bzvtiDisplay_2.Slice = 63
start_data_omega_bzvtiDisplay_2.SelectInputVectors = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_2.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
start_data_omega_bzvtiDisplay_2.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
start_data_omega_bzvtiDisplay_2.ScaleTransferFunction.Points = [-0.7038620845610734, 0.0, 0.5, 0.0, 9.253598515594783, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
start_data_omega_bzvtiDisplay_2.OpacityTransferFunction.Points = [-0.7038620845610734, 0.0, 0.5, 0.0, 9.253598515594783, 1.0, 0.5, 0.0]

# show data from contour1
contour1Display_3 = Show(contour1, renderView2, 'GeometryRepresentation')

# trace defaults for the display properties.
contour1Display_3.Representation = 'Surface'
contour1Display_3.ColorArrayName = ['POINTS', '']
contour1Display_3.LookupTable = omega_bzLUT
contour1Display_3.Opacity = 0.2
contour1Display_3.Specular = 1.0
contour1Display_3.SelectTCoordArray = 'None'
contour1Display_3.SelectNormalArray = 'Normals'
contour1Display_3.SelectTangentArray = 'None'
contour1Display_3.EdgeColor = [0.0, 0.0, 0.0]
contour1Display_3.OSPRayScaleArray = 'omega_bz'
contour1Display_3.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display_3.SelectOrientationVectors = 'None'
contour1Display_3.ScaleFactor = 0.8636709690093994
contour1Display_3.SelectScaleArray = 'omega_bz'
contour1Display_3.GlyphType = 'Arrow'
contour1Display_3.GlyphTableIndexArray = 'omega_bz'
contour1Display_3.GaussianRadius = 0.04318354845046997
contour1Display_3.SetScaleArray = ['POINTS', 'omega_bz']
contour1Display_3.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display_3.OpacityArray = ['POINTS', 'omega_bz']
contour1Display_3.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display_3.DataAxesGrid = 'GridAxesRepresentation'
contour1Display_3.PolarAxes = 'PolarAxesRepresentation'
contour1Display_3.SelectInputVectors = ['POINTS', 'Normals']
contour1Display_3.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
contour1Display_3.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour1Display_3.ScaleTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5001220703125, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour1Display_3.OpacityTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5001220703125, 1.0, 0.5, 0.0]

# show data from tTKIcospheresFromPoints2
tTKIcospheresFromPoints2Display_1 = Show(tTKIcospheresFromPoints2, renderView2, 'GeometryRepresentation')

# trace defaults for the display properties.
tTKIcospheresFromPoints2Display_1.Representation = 'Surface'
tTKIcospheresFromPoints2Display_1.ColorArrayName = ['POINTS', 'CellDimension']
tTKIcospheresFromPoints2Display_1.LookupTable = cellDimensionLUT
tTKIcospheresFromPoints2Display_1.Specular = 1.0
tTKIcospheresFromPoints2Display_1.SelectTCoordArray = 'None'
tTKIcospheresFromPoints2Display_1.SelectNormalArray = 'Normals'
tTKIcospheresFromPoints2Display_1.SelectTangentArray = 'None'
tTKIcospheresFromPoints2Display_1.EdgeColor = [0.0, 0.0, 0.0]
tTKIcospheresFromPoints2Display_1.OSPRayScaleArray = 'CellDimension'
tTKIcospheresFromPoints2Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
tTKIcospheresFromPoints2Display_1.SelectOrientationVectors = 'None'
tTKIcospheresFromPoints2Display_1.ScaleFactor = 0.866682767868042
tTKIcospheresFromPoints2Display_1.SelectScaleArray = 'CellDimension'
tTKIcospheresFromPoints2Display_1.GlyphType = 'Arrow'
tTKIcospheresFromPoints2Display_1.GlyphTableIndexArray = 'CellDimension'
tTKIcospheresFromPoints2Display_1.GaussianRadius = 0.043334138393402104
tTKIcospheresFromPoints2Display_1.SetScaleArray = ['POINTS', 'CellDimension']
tTKIcospheresFromPoints2Display_1.ScaleTransferFunction = 'PiecewiseFunction'
tTKIcospheresFromPoints2Display_1.OpacityArray = ['POINTS', 'CellDimension']
tTKIcospheresFromPoints2Display_1.OpacityTransferFunction = 'PiecewiseFunction'
tTKIcospheresFromPoints2Display_1.DataAxesGrid = 'GridAxesRepresentation'
tTKIcospheresFromPoints2Display_1.PolarAxes = 'PolarAxesRepresentation'
tTKIcospheresFromPoints2Display_1.SelectInputVectors = ['POINTS', 'CellDimension']
tTKIcospheresFromPoints2Display_1.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKIcospheresFromPoints2Display_1.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKIcospheresFromPoints2Display_1.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKIcospheresFromPoints2Display_1.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# show data from tube1
tube1Display = Show(tube1, renderView2, 'GeometryRepresentation')

# trace defaults for the display properties.
tube1Display.Representation = 'Surface'
tube1Display.ColorArrayName = ['CELLS', 'SeparatrixType']
tube1Display.LookupTable = separatrixTypeLUT
tube1Display.Specular = 1.0
tube1Display.SelectTCoordArray = 'None'
tube1Display.SelectNormalArray = 'TubeNormals'
tube1Display.SelectTangentArray = 'None'
tube1Display.EdgeColor = [0.0, 0.0, 0.0]
tube1Display.OSPRayScaleArray = 'CellDimension'
tube1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube1Display.SelectOrientationVectors = 'None'
tube1Display.ScaleFactor = 0.863616418838501
tube1Display.SelectScaleArray = 'SeparatrixType'
tube1Display.GlyphType = 'Arrow'
tube1Display.GlyphTableIndexArray = 'SeparatrixType'
tube1Display.GaussianRadius = 0.04318082094192505
tube1Display.SetScaleArray = ['POINTS', 'CellDimension']
tube1Display.ScaleTransferFunction = 'PiecewiseFunction'
tube1Display.OpacityArray = ['POINTS', 'CellDimension']
tube1Display.OpacityTransferFunction = 'PiecewiseFunction'
tube1Display.DataAxesGrid = 'GridAxesRepresentation'
tube1Display.PolarAxes = 'PolarAxesRepresentation'
tube1Display.SelectInputVectors = ['POINTS', 'CellDimension']
tube1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tube1Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tube1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tube1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# ----------------------------------------------------------------
# setup the visualization in view 'renderView3'
# ----------------------------------------------------------------

# show data from start_data_omega_bzvti
start_data_omega_bzvtiDisplay_3 = Show(start_data_omega_bzvti, renderView3, 'UniformGridRepresentation')

# trace defaults for the display properties.
start_data_omega_bzvtiDisplay_3.Representation = 'Outline'
start_data_omega_bzvtiDisplay_3.ColorArrayName = ['POINTS', '']
start_data_omega_bzvtiDisplay_3.SelectTCoordArray = 'None'
start_data_omega_bzvtiDisplay_3.SelectNormalArray = 'None'
start_data_omega_bzvtiDisplay_3.SelectTangentArray = 'None'
start_data_omega_bzvtiDisplay_3.OSPRayScaleArray = 'bz_wz'
start_data_omega_bzvtiDisplay_3.OSPRayScaleFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay_3.SelectOrientationVectors = 'None'
start_data_omega_bzvtiDisplay_3.ScaleFactor = 1.006182531816462
start_data_omega_bzvtiDisplay_3.SelectScaleArray = 'None'
start_data_omega_bzvtiDisplay_3.GlyphType = 'Arrow'
start_data_omega_bzvtiDisplay_3.GlyphTableIndexArray = 'None'
start_data_omega_bzvtiDisplay_3.GaussianRadius = 0.050309126590823094
start_data_omega_bzvtiDisplay_3.SetScaleArray = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_3.ScaleTransferFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay_3.OpacityArray = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_3.OpacityTransferFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay_3.DataAxesGrid = 'GridAxesRepresentation'
start_data_omega_bzvtiDisplay_3.PolarAxes = 'PolarAxesRepresentation'
start_data_omega_bzvtiDisplay_3.ScalarOpacityUnitDistance = 0.12315087617612483
start_data_omega_bzvtiDisplay_3.OpacityArrayName = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_3.SliceFunction = 'Plane'
start_data_omega_bzvtiDisplay_3.Slice = 63
start_data_omega_bzvtiDisplay_3.SelectInputVectors = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_3.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
start_data_omega_bzvtiDisplay_3.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
start_data_omega_bzvtiDisplay_3.ScaleTransferFunction.Points = [-0.7038620845610734, 0.0, 0.5, 0.0, 9.253598515594783, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
start_data_omega_bzvtiDisplay_3.OpacityTransferFunction.Points = [-0.7038620845610734, 0.0, 0.5, 0.0, 9.253598515594783, 1.0, 0.5, 0.0]

# show data from contour1
contour1Display_4 = Show(contour1, renderView3, 'GeometryRepresentation')

# trace defaults for the display properties.
contour1Display_4.Representation = 'Surface'
contour1Display_4.ColorArrayName = ['POINTS', '']
contour1Display_4.LookupTable = omega_bzLUT
contour1Display_4.Opacity = 0.2
contour1Display_4.Specular = 1.0
contour1Display_4.SelectTCoordArray = 'None'
contour1Display_4.SelectNormalArray = 'Normals'
contour1Display_4.SelectTangentArray = 'None'
contour1Display_4.EdgeColor = [0.0, 0.0, 0.0]
contour1Display_4.OSPRayScaleArray = 'omega_bz'
contour1Display_4.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display_4.SelectOrientationVectors = 'None'
contour1Display_4.ScaleFactor = 0.8636709690093994
contour1Display_4.SelectScaleArray = 'omega_bz'
contour1Display_4.GlyphType = 'Arrow'
contour1Display_4.GlyphTableIndexArray = 'omega_bz'
contour1Display_4.GaussianRadius = 0.04318354845046997
contour1Display_4.SetScaleArray = ['POINTS', 'omega_bz']
contour1Display_4.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display_4.OpacityArray = ['POINTS', 'omega_bz']
contour1Display_4.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display_4.DataAxesGrid = 'GridAxesRepresentation'
contour1Display_4.PolarAxes = 'PolarAxesRepresentation'
contour1Display_4.SelectInputVectors = ['POINTS', 'Normals']
contour1Display_4.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
contour1Display_4.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour1Display_4.ScaleTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5001220703125, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour1Display_4.OpacityTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5001220703125, 1.0, 0.5, 0.0]

# show data from tTKGeometrySmoother2
tTKGeometrySmoother2Display_1 = Show(tTKGeometrySmoother2, renderView3, 'UnstructuredGridRepresentation')

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
tTKGeometrySmoother2Display_1.Representation = 'Surface'
tTKGeometrySmoother2Display_1.ColorArrayName = ['CELLS', 'Persistence']
tTKGeometrySmoother2Display_1.LookupTable = persistenceLUT
tTKGeometrySmoother2Display_1.LineWidth = 10.0
tTKGeometrySmoother2Display_1.RenderLinesAsTubes = 1
tTKGeometrySmoother2Display_1.Specular = 1.0
tTKGeometrySmoother2Display_1.SelectTCoordArray = 'None'
tTKGeometrySmoother2Display_1.SelectNormalArray = 'None'
tTKGeometrySmoother2Display_1.SelectTangentArray = 'None'
tTKGeometrySmoother2Display_1.OSPRayScaleArray = 'oppositeOmega'
tTKGeometrySmoother2Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
tTKGeometrySmoother2Display_1.SelectOrientationVectors = 'None'
tTKGeometrySmoother2Display_1.ScaleFactor = 0.07141872048377991
tTKGeometrySmoother2Display_1.SelectScaleArray = 'None'
tTKGeometrySmoother2Display_1.GlyphType = 'Arrow'
tTKGeometrySmoother2Display_1.GlyphTableIndexArray = 'None'
tTKGeometrySmoother2Display_1.GaussianRadius = 0.0035709360241889952
tTKGeometrySmoother2Display_1.SetScaleArray = ['POINTS', 'oppositeOmega']
tTKGeometrySmoother2Display_1.ScaleTransferFunction = 'PiecewiseFunction'
tTKGeometrySmoother2Display_1.OpacityArray = ['POINTS', 'oppositeOmega']
tTKGeometrySmoother2Display_1.OpacityTransferFunction = 'PiecewiseFunction'
tTKGeometrySmoother2Display_1.DataAxesGrid = 'GridAxesRepresentation'
tTKGeometrySmoother2Display_1.PolarAxes = 'PolarAxesRepresentation'
tTKGeometrySmoother2Display_1.ScalarOpacityFunction = persistencePWF
tTKGeometrySmoother2Display_1.ScalarOpacityUnitDistance = 0.21744076418518754
tTKGeometrySmoother2Display_1.OpacityArrayName = ['POINTS', 'oppositeOmega']
tTKGeometrySmoother2Display_1.SelectInputVectors = ['POINTS', 'oppositeOmega']
tTKGeometrySmoother2Display_1.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKGeometrySmoother2Display_1.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKGeometrySmoother2Display_1.ScaleTransferFunction.Points = [-0.9751526647579255, 0.0, 0.5, 0.0, -0.9056711359213363, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKGeometrySmoother2Display_1.OpacityTransferFunction.Points = [-0.9751526647579255, 0.0, 0.5, 0.0, -0.9056711359213363, 1.0, 0.5, 0.0]

# show data from tTKPersistentGenerators1
tTKPersistentGenerators1Display = Show(tTKPersistentGenerators1, renderView3, 'GeometryRepresentation')

# trace defaults for the display properties.
tTKPersistentGenerators1Display.Representation = 'Surface'
tTKPersistentGenerators1Display.ColorArrayName = ['POINTS', '']
tTKPersistentGenerators1Display.Specular = 1.0
tTKPersistentGenerators1Display.SelectTCoordArray = 'None'
tTKPersistentGenerators1Display.SelectNormalArray = 'None'
tTKPersistentGenerators1Display.SelectTangentArray = 'None'
tTKPersistentGenerators1Display.EdgeColor = [0.0, 0.0, 0.0]
tTKPersistentGenerators1Display.OSPRayScaleArray = 'oppositeOmega'
tTKPersistentGenerators1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKPersistentGenerators1Display.SelectOrientationVectors = 'None'
tTKPersistentGenerators1Display.ScaleFactor = 1.0061824798583985
tTKPersistentGenerators1Display.SelectScaleArray = 'None'
tTKPersistentGenerators1Display.GlyphType = 'Arrow'
tTKPersistentGenerators1Display.GlyphTableIndexArray = 'None'
tTKPersistentGenerators1Display.GaussianRadius = 0.050309123992919924
tTKPersistentGenerators1Display.SetScaleArray = ['POINTS', 'oppositeOmega']
tTKPersistentGenerators1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKPersistentGenerators1Display.OpacityArray = ['POINTS', 'oppositeOmega']
tTKPersistentGenerators1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKPersistentGenerators1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKPersistentGenerators1Display.PolarAxes = 'PolarAxesRepresentation'
tTKPersistentGenerators1Display.SelectInputVectors = ['POINTS', 'oppositeOmega']
tTKPersistentGenerators1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKPersistentGenerators1Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKPersistentGenerators1Display.ScaleTransferFunction.Points = [-0.9949202085539145, 0.0, 0.5, 0.0, -0.0064376340156840905, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKPersistentGenerators1Display.OpacityTransferFunction.Points = [-0.9949202085539145, 0.0, 0.5, 0.0, -0.0064376340156840905, 1.0, 0.5, 0.0]

# hide data in view
Hide(tTKPersistentGenerators1, renderView3)

# ----------------------------------------------------------------
# setup the visualization in view 'renderView4'
# ----------------------------------------------------------------

# show data from start_data_omega_bzvti
start_data_omega_bzvtiDisplay_4 = Show(start_data_omega_bzvti, renderView4, 'UniformGridRepresentation')

# trace defaults for the display properties.
start_data_omega_bzvtiDisplay_4.Representation = 'Outline'
start_data_omega_bzvtiDisplay_4.ColorArrayName = ['POINTS', '']
start_data_omega_bzvtiDisplay_4.SelectTCoordArray = 'None'
start_data_omega_bzvtiDisplay_4.SelectNormalArray = 'None'
start_data_omega_bzvtiDisplay_4.SelectTangentArray = 'None'
start_data_omega_bzvtiDisplay_4.OSPRayScaleArray = 'bz_wz'
start_data_omega_bzvtiDisplay_4.OSPRayScaleFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay_4.SelectOrientationVectors = 'None'
start_data_omega_bzvtiDisplay_4.ScaleFactor = 1.006182531816462
start_data_omega_bzvtiDisplay_4.SelectScaleArray = 'None'
start_data_omega_bzvtiDisplay_4.GlyphType = 'Arrow'
start_data_omega_bzvtiDisplay_4.GlyphTableIndexArray = 'None'
start_data_omega_bzvtiDisplay_4.GaussianRadius = 0.050309126590823094
start_data_omega_bzvtiDisplay_4.SetScaleArray = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_4.ScaleTransferFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay_4.OpacityArray = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_4.OpacityTransferFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay_4.DataAxesGrid = 'GridAxesRepresentation'
start_data_omega_bzvtiDisplay_4.PolarAxes = 'PolarAxesRepresentation'
start_data_omega_bzvtiDisplay_4.ScalarOpacityUnitDistance = 0.12315087617612483
start_data_omega_bzvtiDisplay_4.OpacityArrayName = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_4.SliceFunction = 'Plane'
start_data_omega_bzvtiDisplay_4.Slice = 63
start_data_omega_bzvtiDisplay_4.SelectInputVectors = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_4.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
start_data_omega_bzvtiDisplay_4.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
start_data_omega_bzvtiDisplay_4.ScaleTransferFunction.Points = [-0.7038620845610734, 0.0, 0.5, 0.0, 9.253598515594783, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
start_data_omega_bzvtiDisplay_4.OpacityTransferFunction.Points = [-0.7038620845610734, 0.0, 0.5, 0.0, 9.253598515594783, 1.0, 0.5, 0.0]

# show data from contour1
contour1Display_5 = Show(contour1, renderView4, 'GeometryRepresentation')

# trace defaults for the display properties.
contour1Display_5.Representation = 'Surface'
contour1Display_5.ColorArrayName = ['POINTS', '']
contour1Display_5.LookupTable = omega_bzLUT
contour1Display_5.Opacity = 0.1
contour1Display_5.Specular = 1.0
contour1Display_5.SelectTCoordArray = 'None'
contour1Display_5.SelectNormalArray = 'Normals'
contour1Display_5.SelectTangentArray = 'None'
contour1Display_5.EdgeColor = [0.0, 0.0, 0.0]
contour1Display_5.OSPRayScaleArray = 'omega_bz'
contour1Display_5.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display_5.SelectOrientationVectors = 'None'
contour1Display_5.ScaleFactor = 0.8636709690093994
contour1Display_5.SelectScaleArray = 'omega_bz'
contour1Display_5.GlyphType = 'Arrow'
contour1Display_5.GlyphTableIndexArray = 'omega_bz'
contour1Display_5.GaussianRadius = 0.04318354845046997
contour1Display_5.SetScaleArray = ['POINTS', 'omega_bz']
contour1Display_5.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display_5.OpacityArray = ['POINTS', 'omega_bz']
contour1Display_5.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display_5.DataAxesGrid = 'GridAxesRepresentation'
contour1Display_5.PolarAxes = 'PolarAxesRepresentation'
contour1Display_5.SelectInputVectors = ['POINTS', 'Normals']
contour1Display_5.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
contour1Display_5.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour1Display_5.ScaleTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5001220703125, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour1Display_5.OpacityTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5001220703125, 1.0, 0.5, 0.0]

# show data from threshold3
threshold3Display = Show(threshold3, renderView4, 'UnstructuredGridRepresentation')

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
# setup the visualization in view 'renderView5'
# ----------------------------------------------------------------

# show data from start_data_omega_bzvti
start_data_omega_bzvtiDisplay_5 = Show(start_data_omega_bzvti, renderView5, 'UniformGridRepresentation')

# trace defaults for the display properties.
start_data_omega_bzvtiDisplay_5.Representation = 'Outline'
start_data_omega_bzvtiDisplay_5.AmbientColor = [0.1803921568627451, 0.17647058823529413, 0.17647058823529413]
start_data_omega_bzvtiDisplay_5.ColorArrayName = ['POINTS', '']
start_data_omega_bzvtiDisplay_5.DiffuseColor = [0.1803921568627451, 0.17647058823529413, 0.17647058823529413]
start_data_omega_bzvtiDisplay_5.SelectTCoordArray = 'None'
start_data_omega_bzvtiDisplay_5.SelectNormalArray = 'None'
start_data_omega_bzvtiDisplay_5.SelectTangentArray = 'None'
start_data_omega_bzvtiDisplay_5.OSPRayScaleArray = 'bz_wz'
start_data_omega_bzvtiDisplay_5.OSPRayScaleFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay_5.SelectOrientationVectors = 'None'
start_data_omega_bzvtiDisplay_5.ScaleFactor = 1.006182531816462
start_data_omega_bzvtiDisplay_5.SelectScaleArray = 'None'
start_data_omega_bzvtiDisplay_5.GlyphType = 'Arrow'
start_data_omega_bzvtiDisplay_5.GlyphTableIndexArray = 'None'
start_data_omega_bzvtiDisplay_5.GaussianRadius = 0.050309126590823094
start_data_omega_bzvtiDisplay_5.SetScaleArray = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_5.ScaleTransferFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay_5.OpacityArray = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_5.OpacityTransferFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay_5.DataAxesGrid = 'GridAxesRepresentation'
start_data_omega_bzvtiDisplay_5.PolarAxes = 'PolarAxesRepresentation'
start_data_omega_bzvtiDisplay_5.ScalarOpacityUnitDistance = 0.12315087617612483
start_data_omega_bzvtiDisplay_5.OpacityArrayName = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_5.SliceFunction = 'Plane'
start_data_omega_bzvtiDisplay_5.Slice = 63
start_data_omega_bzvtiDisplay_5.SelectInputVectors = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_5.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
start_data_omega_bzvtiDisplay_5.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
start_data_omega_bzvtiDisplay_5.ScaleTransferFunction.Points = [-0.7038620845610734, 0.0, 0.5, 0.0, 9.253598515594783, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
start_data_omega_bzvtiDisplay_5.OpacityTransferFunction.Points = [-0.7038620845610734, 0.0, 0.5, 0.0, 9.253598515594783, 1.0, 0.5, 0.0]

# show data from contour1
contour1Display_6 = Show(contour1, renderView5, 'GeometryRepresentation')

# get color transfer function/color map for 'bz_wz'
bz_wzLUT = GetColorTransferFunction('bz_wz')
bz_wzLUT.RGBPoints = [-0.36186845055807093, 0.0, 0.129412, 0.584314, 3.788039026700919, 0.917647, 0.941176, 0.788235, 7.937946503959902, 0.0, 0.431373, 0.0]
bz_wzLUT.ColorSpace = 'RGB'
bz_wzLUT.AboveRangeColor = [1.0, 1.0, 1.0]
bz_wzLUT.NanColor = [0.0, 0.0, 0.0]
bz_wzLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
contour1Display_6.Representation = 'Surface'
contour1Display_6.ColorArrayName = ['POINTS', 'bz_wz']
contour1Display_6.LookupTable = bz_wzLUT
contour1Display_6.Specular = 1.0
contour1Display_6.SelectTCoordArray = 'None'
contour1Display_6.SelectNormalArray = 'Normals'
contour1Display_6.SelectTangentArray = 'None'
contour1Display_6.EdgeColor = [0.0, 0.0, 0.0]
contour1Display_6.OSPRayScaleArray = 'omega_bz'
contour1Display_6.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display_6.SelectOrientationVectors = 'None'
contour1Display_6.ScaleFactor = 0.8636709690093994
contour1Display_6.SelectScaleArray = 'omega_bz'
contour1Display_6.GlyphType = 'Arrow'
contour1Display_6.GlyphTableIndexArray = 'omega_bz'
contour1Display_6.GaussianRadius = 0.04318354845046997
contour1Display_6.SetScaleArray = ['POINTS', 'omega_bz']
contour1Display_6.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display_6.OpacityArray = ['POINTS', 'omega_bz']
contour1Display_6.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display_6.DataAxesGrid = 'GridAxesRepresentation'
contour1Display_6.PolarAxes = 'PolarAxesRepresentation'
contour1Display_6.SelectInputVectors = ['POINTS', 'Normals']
contour1Display_6.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
contour1Display_6.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour1Display_6.ScaleTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5001220703125, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour1Display_6.OpacityTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5001220703125, 1.0, 0.5, 0.0]

# show data from slice1
slice1Display_2 = Show(slice1, renderView5, 'GeometryRepresentation')

# trace defaults for the display properties.
slice1Display_2.Representation = 'Surface'
slice1Display_2.ColorArrayName = ['POINTS', 'Bz']
slice1Display_2.LookupTable = bzLUT
slice1Display_2.Specular = 1.0
slice1Display_2.SelectTCoordArray = 'None'
slice1Display_2.SelectNormalArray = 'None'
slice1Display_2.SelectTangentArray = 'None'
slice1Display_2.EdgeColor = [0.0, 0.0, 0.0]
slice1Display_2.OSPRayScaleArray = 'Bz'
slice1Display_2.OSPRayScaleFunction = 'PiecewiseFunction'
slice1Display_2.SelectOrientationVectors = 'Bz'
slice1Display_2.ScaleFactor = 1.0061825752258302
slice1Display_2.SelectScaleArray = 'Bz'
slice1Display_2.GlyphType = 'Arrow'
slice1Display_2.GlyphTableIndexArray = 'Bz'
slice1Display_2.GaussianRadius = 0.050309128761291504
slice1Display_2.SetScaleArray = ['POINTS', 'Bz']
slice1Display_2.ScaleTransferFunction = 'PiecewiseFunction'
slice1Display_2.OpacityArray = ['POINTS', 'Bz']
slice1Display_2.OpacityTransferFunction = 'PiecewiseFunction'
slice1Display_2.DataAxesGrid = 'GridAxesRepresentation'
slice1Display_2.PolarAxes = 'PolarAxesRepresentation'
slice1Display_2.SelectInputVectors = ['POINTS', 'Bz']
slice1Display_2.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
slice1Display_2.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice1Display_2.ScaleTransferFunction.Points = [-0.4143731230557486, 0.0, 0.5, 0.0, 0.41437312305574814, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice1Display_2.OpacityTransferFunction.Points = [-0.4143731230557486, 0.0, 0.5, 0.0, 0.41437312305574814, 1.0, 0.5, 0.0]

# hide data in view
Hide(slice1, renderView5)

# ----------------------------------------------------------------
# setup the visualization in view 'renderView6'
# ----------------------------------------------------------------

# show data from contour1
contour1Display_7 = Show(contour1, renderView6, 'GeometryRepresentation')

# trace defaults for the display properties.
contour1Display_7.Representation = 'Surface'
contour1Display_7.ColorArrayName = ['POINTS', 'bz_wz']
contour1Display_7.LookupTable = bz_wzLUT
contour1Display_7.Specular = 1.0
contour1Display_7.SelectTCoordArray = 'None'
contour1Display_7.SelectNormalArray = 'Normals'
contour1Display_7.SelectTangentArray = 'None'
contour1Display_7.EdgeColor = [0.0, 0.0, 0.0]
contour1Display_7.OSPRayScaleArray = 'omega_bz'
contour1Display_7.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display_7.SelectOrientationVectors = 'None'
contour1Display_7.ScaleFactor = 0.8636709690093994
contour1Display_7.SelectScaleArray = 'omega_bz'
contour1Display_7.GlyphType = 'Arrow'
contour1Display_7.GlyphTableIndexArray = 'omega_bz'
contour1Display_7.GaussianRadius = 0.04318354845046997
contour1Display_7.SetScaleArray = ['POINTS', 'omega_bz']
contour1Display_7.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display_7.OpacityArray = ['POINTS', 'omega_bz']
contour1Display_7.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display_7.DataAxesGrid = 'GridAxesRepresentation'
contour1Display_7.PolarAxes = 'PolarAxesRepresentation'
contour1Display_7.SelectInputVectors = ['POINTS', 'Normals']
contour1Display_7.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
contour1Display_7.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour1Display_7.ScaleTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5001220703125, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour1Display_7.OpacityTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5001220703125, 1.0, 0.5, 0.0]

# show data from start_data_omega_bzvti
start_data_omega_bzvtiDisplay_6 = Show(start_data_omega_bzvti, renderView6, 'UniformGridRepresentation')

# trace defaults for the display properties.
start_data_omega_bzvtiDisplay_6.Representation = 'Outline'
start_data_omega_bzvtiDisplay_6.AmbientColor = [0.1803921568627451, 0.17647058823529413, 0.17647058823529413]
start_data_omega_bzvtiDisplay_6.ColorArrayName = ['POINTS', '']
start_data_omega_bzvtiDisplay_6.DiffuseColor = [0.1803921568627451, 0.17647058823529413, 0.17647058823529413]
start_data_omega_bzvtiDisplay_6.SelectTCoordArray = 'None'
start_data_omega_bzvtiDisplay_6.SelectNormalArray = 'None'
start_data_omega_bzvtiDisplay_6.SelectTangentArray = 'None'
start_data_omega_bzvtiDisplay_6.OSPRayScaleArray = 'bz_wz'
start_data_omega_bzvtiDisplay_6.OSPRayScaleFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay_6.SelectOrientationVectors = 'None'
start_data_omega_bzvtiDisplay_6.ScaleFactor = 1.006182531816462
start_data_omega_bzvtiDisplay_6.SelectScaleArray = 'None'
start_data_omega_bzvtiDisplay_6.GlyphType = 'Arrow'
start_data_omega_bzvtiDisplay_6.GlyphTableIndexArray = 'None'
start_data_omega_bzvtiDisplay_6.GaussianRadius = 0.050309126590823094
start_data_omega_bzvtiDisplay_6.SetScaleArray = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_6.ScaleTransferFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay_6.OpacityArray = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_6.OpacityTransferFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay_6.DataAxesGrid = 'GridAxesRepresentation'
start_data_omega_bzvtiDisplay_6.PolarAxes = 'PolarAxesRepresentation'
start_data_omega_bzvtiDisplay_6.ScalarOpacityUnitDistance = 0.12315087617612483
start_data_omega_bzvtiDisplay_6.OpacityArrayName = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_6.SliceFunction = 'Plane'
start_data_omega_bzvtiDisplay_6.Slice = 63
start_data_omega_bzvtiDisplay_6.SelectInputVectors = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_6.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
start_data_omega_bzvtiDisplay_6.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
start_data_omega_bzvtiDisplay_6.ScaleTransferFunction.Points = [-0.7038620845610734, 0.0, 0.5, 0.0, 9.253598515594783, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
start_data_omega_bzvtiDisplay_6.OpacityTransferFunction.Points = [-0.7038620845610734, 0.0, 0.5, 0.0, 9.253598515594783, 1.0, 0.5, 0.0]

# show data from connectivity1
connectivity1Display = Show(connectivity1, renderView6, 'GeometryRepresentation')

# get color transfer function/color map for 'RegionId'
regionIdLUT = GetColorTransferFunction('RegionId')
regionIdLUT.RGBPoints = [0.0, 0.0, 0.129412, 0.584314, 1.5000000000000013, 0.917647, 0.941176, 0.788235, 3.0, 0.0, 0.431373, 0.0]
regionIdLUT.ColorSpace = 'RGB'
regionIdLUT.AboveRangeColor = [1.0, 1.0, 1.0]
regionIdLUT.NanColor = [0.0, 0.0, 0.0]
regionIdLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
connectivity1Display.Representation = 'Surface'
connectivity1Display.ColorArrayName = ['POINTS', 'RegionId']
connectivity1Display.LookupTable = regionIdLUT
connectivity1Display.Specular = 1.0
connectivity1Display.SelectTCoordArray = 'None'
connectivity1Display.SelectNormalArray = 'Normals'
connectivity1Display.SelectTangentArray = 'None'
connectivity1Display.EdgeColor = [0.0, 0.0, 0.0]
connectivity1Display.OSPRayScaleArray = 'RegionId'
connectivity1Display.OSPRayScaleFunction = 'PiecewiseFunction'
connectivity1Display.SelectOrientationVectors = 'None'
connectivity1Display.ScaleFactor = 0.8636709690093994
connectivity1Display.SelectScaleArray = 'RegionId'
connectivity1Display.GlyphType = 'Arrow'
connectivity1Display.GlyphTableIndexArray = 'RegionId'
connectivity1Display.GaussianRadius = 0.04318354845046997
connectivity1Display.SetScaleArray = ['POINTS', 'RegionId']
connectivity1Display.ScaleTransferFunction = 'PiecewiseFunction'
connectivity1Display.OpacityArray = ['POINTS', 'RegionId']
connectivity1Display.OpacityTransferFunction = 'PiecewiseFunction'
connectivity1Display.DataAxesGrid = 'GridAxesRepresentation'
connectivity1Display.PolarAxes = 'PolarAxesRepresentation'
connectivity1Display.SelectInputVectors = ['POINTS', 'Normals']
connectivity1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
connectivity1Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
connectivity1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
connectivity1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# show data from threshold4
threshold4Display = Show(threshold4, renderView6, 'UnstructuredGridRepresentation')

# get opacity transfer function/opacity map for 'bz_wz'
bz_wzPWF = GetOpacityTransferFunction('bz_wz')
bz_wzPWF.Points = [-0.36186845055807093, 0.0, 0.5, 0.0, 7.937946503959902, 1.0, 0.5, 0.0]
bz_wzPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
threshold4Display.Representation = 'Surface'
threshold4Display.ColorArrayName = ['POINTS', 'bz_wz']
threshold4Display.LookupTable = bz_wzLUT
threshold4Display.Opacity = 0.3
threshold4Display.Specular = 1.0
threshold4Display.SelectTCoordArray = 'None'
threshold4Display.SelectNormalArray = 'Normals'
threshold4Display.SelectTangentArray = 'None'
threshold4Display.OSPRayScaleArray = 'RegionId'
threshold4Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold4Display.SelectOrientationVectors = 'None'
threshold4Display.ScaleFactor = 0.3055371522903443
threshold4Display.SelectScaleArray = 'RegionId'
threshold4Display.GlyphType = 'Arrow'
threshold4Display.GlyphTableIndexArray = 'RegionId'
threshold4Display.GaussianRadius = 0.015276857614517213
threshold4Display.SetScaleArray = ['POINTS', 'RegionId']
threshold4Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold4Display.OpacityArray = ['POINTS', 'RegionId']
threshold4Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold4Display.DataAxesGrid = 'GridAxesRepresentation'
threshold4Display.PolarAxes = 'PolarAxesRepresentation'
threshold4Display.ScalarOpacityFunction = bz_wzPWF
threshold4Display.ScalarOpacityUnitDistance = 0.1864963582339875
threshold4Display.OpacityArrayName = ['POINTS', 'RegionId']
threshold4Display.SelectInputVectors = ['POINTS', 'Normals']
threshold4Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
threshold4Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold4Display.ScaleTransferFunction.Points = [2.0, 0.0, 0.5, 0.0, 2.00048828125, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold4Display.OpacityTransferFunction.Points = [2.0, 0.0, 0.5, 0.0, 2.00048828125, 1.0, 0.5, 0.0]

# show data from contour2
contour2Display = Show(contour2, renderView6, 'GeometryRepresentation')

# trace defaults for the display properties.
contour2Display.Representation = 'Surface'
contour2Display.ColorArrayName = ['POINTS', 'omega_bz']
contour2Display.LookupTable = omega_bzLUT
contour2Display.Specular = 1.0
contour2Display.SelectTCoordArray = 'None'
contour2Display.SelectNormalArray = 'Normals'
contour2Display.SelectTangentArray = 'None'
contour2Display.EdgeColor = [0.0, 0.0, 0.0]
contour2Display.OSPRayScaleArray = 'omega_bz'
contour2Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour2Display.SelectOrientationVectors = 'None'
contour2Display.ScaleFactor = 0.8636709690093994
contour2Display.SelectScaleArray = 'omega_bz'
contour2Display.GlyphType = 'Arrow'
contour2Display.GlyphTableIndexArray = 'omega_bz'
contour2Display.GaussianRadius = 0.04318354845046997
contour2Display.SetScaleArray = ['POINTS', 'omega_bz']
contour2Display.ScaleTransferFunction = 'PiecewiseFunction'
contour2Display.OpacityArray = ['POINTS', 'omega_bz']
contour2Display.OpacityTransferFunction = 'PiecewiseFunction'
contour2Display.DataAxesGrid = 'GridAxesRepresentation'
contour2Display.PolarAxes = 'PolarAxesRepresentation'
contour2Display.SelectInputVectors = ['POINTS', 'Normals']
contour2Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
contour2Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour2Display.ScaleTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5001220703125, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour2Display.OpacityTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5001220703125, 1.0, 0.5, 0.0]

# show data from connectivity2
connectivity2Display = Show(connectivity2, renderView6, 'GeometryRepresentation')

# trace defaults for the display properties.
connectivity2Display.Representation = 'Surface'
connectivity2Display.ColorArrayName = ['POINTS', 'RegionId']
connectivity2Display.LookupTable = regionIdLUT
connectivity2Display.Specular = 1.0
connectivity2Display.SelectTCoordArray = 'None'
connectivity2Display.SelectNormalArray = 'Normals'
connectivity2Display.SelectTangentArray = 'None'
connectivity2Display.EdgeColor = [0.0, 0.0, 0.0]
connectivity2Display.OSPRayScaleArray = 'RegionId'
connectivity2Display.OSPRayScaleFunction = 'PiecewiseFunction'
connectivity2Display.SelectOrientationVectors = 'None'
connectivity2Display.ScaleFactor = 0.846682643890381
connectivity2Display.SelectScaleArray = 'RegionId'
connectivity2Display.GlyphType = 'Arrow'
connectivity2Display.GlyphTableIndexArray = 'RegionId'
connectivity2Display.GaussianRadius = 0.04233413219451904
connectivity2Display.SetScaleArray = ['POINTS', 'RegionId']
connectivity2Display.ScaleTransferFunction = 'PiecewiseFunction'
connectivity2Display.OpacityArray = ['POINTS', 'RegionId']
connectivity2Display.OpacityTransferFunction = 'PiecewiseFunction'
connectivity2Display.DataAxesGrid = 'GridAxesRepresentation'
connectivity2Display.PolarAxes = 'PolarAxesRepresentation'
connectivity2Display.SelectInputVectors = ['POINTS', 'Normals']
connectivity2Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
connectivity2Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# show data from threshold6
threshold6Display = Show(threshold6, renderView6, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
threshold6Display.Representation = 'Surface'
threshold6Display.ColorArrayName = ['POINTS', 'bz_wz']
threshold6Display.LookupTable = bz_wzLUT
threshold6Display.Opacity = 0.3
threshold6Display.Specular = 1.0
threshold6Display.SelectTCoordArray = 'None'
threshold6Display.SelectNormalArray = 'Normals'
threshold6Display.SelectTangentArray = 'None'
threshold6Display.OSPRayScaleArray = 'RegionId'
threshold6Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold6Display.SelectOrientationVectors = 'None'
threshold6Display.ScaleFactor = 0.270881986618042
threshold6Display.SelectScaleArray = 'RegionId'
threshold6Display.GlyphType = 'Arrow'
threshold6Display.GlyphTableIndexArray = 'RegionId'
threshold6Display.GaussianRadius = 0.0135440993309021
threshold6Display.SetScaleArray = ['POINTS', 'RegionId']
threshold6Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold6Display.OpacityArray = ['POINTS', 'RegionId']
threshold6Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold6Display.DataAxesGrid = 'GridAxesRepresentation'
threshold6Display.PolarAxes = 'PolarAxesRepresentation'
threshold6Display.ScalarOpacityFunction = bz_wzPWF
threshold6Display.ScalarOpacityUnitDistance = 0.19660327886133
threshold6Display.OpacityArrayName = ['POINTS', 'RegionId']
threshold6Display.SelectInputVectors = ['POINTS', 'Normals']
threshold6Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
threshold6Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold6Display.ScaleTransferFunction.Points = [1.0, 0.0, 0.5, 0.0, 1.000244140625, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold6Display.OpacityTransferFunction.Points = [1.0, 0.0, 0.5, 0.0, 1.000244140625, 1.0, 0.5, 0.0]

# show data from contour3
contour3Display = Show(contour3, renderView6, 'GeometryRepresentation')

# trace defaults for the display properties.
contour3Display.Representation = 'Surface'
contour3Display.ColorArrayName = ['POINTS', 'omega_bz']
contour3Display.LookupTable = omega_bzLUT
contour3Display.Specular = 1.0
contour3Display.SelectTCoordArray = 'None'
contour3Display.SelectNormalArray = 'Normals'
contour3Display.SelectTangentArray = 'None'
contour3Display.EdgeColor = [0.0, 0.0, 0.0]
contour3Display.OSPRayScaleArray = 'omega_bz'
contour3Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour3Display.SelectOrientationVectors = 'None'
contour3Display.ScaleFactor = 0.846682643890381
contour3Display.SelectScaleArray = 'omega_bz'
contour3Display.GlyphType = 'Arrow'
contour3Display.GlyphTableIndexArray = 'omega_bz'
contour3Display.GaussianRadius = 0.04233413219451904
contour3Display.SetScaleArray = ['POINTS', 'omega_bz']
contour3Display.ScaleTransferFunction = 'PiecewiseFunction'
contour3Display.OpacityArray = ['POINTS', 'omega_bz']
contour3Display.OpacityTransferFunction = 'PiecewiseFunction'
contour3Display.DataAxesGrid = 'GridAxesRepresentation'
contour3Display.PolarAxes = 'PolarAxesRepresentation'
contour3Display.SelectInputVectors = ['POINTS', 'Normals']
contour3Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
contour3Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour3Display.ScaleTransferFunction.Points = [0.949999988079071, 0.0, 0.5, 0.0, 0.950122058391571, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour3Display.OpacityTransferFunction.Points = [0.949999988079071, 0.0, 0.5, 0.0, 0.950122058391571, 1.0, 0.5, 0.0]

# show data from connectivity3
connectivity3Display = Show(connectivity3, renderView6, 'GeometryRepresentation')

# trace defaults for the display properties.
connectivity3Display.Representation = 'Surface'
connectivity3Display.ColorArrayName = ['POINTS', 'RegionId']
connectivity3Display.LookupTable = regionIdLUT
connectivity3Display.Specular = 1.0
connectivity3Display.SelectTCoordArray = 'None'
connectivity3Display.SelectNormalArray = 'Normals'
connectivity3Display.SelectTangentArray = 'None'
connectivity3Display.EdgeColor = [0.0, 0.0, 0.0]
connectivity3Display.OSPRayScaleArray = 'RegionId'
connectivity3Display.OSPRayScaleFunction = 'PiecewiseFunction'
connectivity3Display.SelectOrientationVectors = 'None'
connectivity3Display.ScaleFactor = 0.846682643890381
connectivity3Display.SelectScaleArray = 'RegionId'
connectivity3Display.GlyphType = 'Arrow'
connectivity3Display.GlyphTableIndexArray = 'RegionId'
connectivity3Display.GaussianRadius = 0.04233413219451904
connectivity3Display.SetScaleArray = ['POINTS', 'RegionId']
connectivity3Display.ScaleTransferFunction = 'PiecewiseFunction'
connectivity3Display.OpacityArray = ['POINTS', 'RegionId']
connectivity3Display.OpacityTransferFunction = 'PiecewiseFunction'
connectivity3Display.DataAxesGrid = 'GridAxesRepresentation'
connectivity3Display.PolarAxes = 'PolarAxesRepresentation'
connectivity3Display.SelectInputVectors = ['POINTS', 'Normals']
connectivity3Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
connectivity3Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
connectivity3Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
connectivity3Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.0, 1.0, 0.5, 0.0]

# show data from threshold7
threshold7Display = Show(threshold7, renderView6, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
threshold7Display.Representation = 'Surface'
threshold7Display.ColorArrayName = ['POINTS', 'bz_wz']
threshold7Display.LookupTable = bz_wzLUT
threshold7Display.Specular = 1.0
threshold7Display.SelectTCoordArray = 'None'
threshold7Display.SelectNormalArray = 'Normals'
threshold7Display.SelectTangentArray = 'None'
threshold7Display.OSPRayScaleArray = 'RegionId'
threshold7Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold7Display.SelectOrientationVectors = 'None'
threshold7Display.ScaleFactor = 0.2549871921539307
threshold7Display.SelectScaleArray = 'RegionId'
threshold7Display.GlyphType = 'Arrow'
threshold7Display.GlyphTableIndexArray = 'RegionId'
threshold7Display.GaussianRadius = 0.012749359607696534
threshold7Display.SetScaleArray = ['POINTS', 'RegionId']
threshold7Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold7Display.OpacityArray = ['POINTS', 'RegionId']
threshold7Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold7Display.DataAxesGrid = 'GridAxesRepresentation'
threshold7Display.PolarAxes = 'PolarAxesRepresentation'
threshold7Display.ScalarOpacityFunction = bz_wzPWF
threshold7Display.ScalarOpacityUnitDistance = 0.2430388853433246
threshold7Display.OpacityArrayName = ['POINTS', 'RegionId']
threshold7Display.SelectInputVectors = ['POINTS', 'Normals']
threshold7Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
threshold7Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold7Display.ScaleTransferFunction.Points = [1.0, 0.0, 0.5, 0.0, 2.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold7Display.OpacityTransferFunction.Points = [1.0, 0.0, 0.5, 0.0, 2.0, 1.0, 0.5, 0.0]

# show data from tube7
tube7Display_1 = Show(tube7, renderView6, 'GeometryRepresentation')

# trace defaults for the display properties.
tube7Display_1.Representation = 'Surface'
tube7Display_1.ColorArrayName = [None, '']
tube7Display_1.Specular = 1.0
tube7Display_1.SelectTCoordArray = 'None'
tube7Display_1.SelectNormalArray = 'TubeNormals'
tube7Display_1.SelectTangentArray = 'None'
tube7Display_1.EdgeColor = [0.0, 0.0, 0.0]
tube7Display_1.OSPRayScaleArray = 'AngularVelocity'
tube7Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
tube7Display_1.SelectOrientationVectors = 'Normals'
tube7Display_1.ScaleFactor = 0.28432756662368774
tube7Display_1.SelectScaleArray = 'AngularVelocity'
tube7Display_1.GlyphType = 'Arrow'
tube7Display_1.GlyphTableIndexArray = 'AngularVelocity'
tube7Display_1.GaussianRadius = 0.014216378331184387
tube7Display_1.SetScaleArray = ['POINTS', 'AngularVelocity']
tube7Display_1.ScaleTransferFunction = 'PiecewiseFunction'
tube7Display_1.OpacityArray = ['POINTS', 'AngularVelocity']
tube7Display_1.OpacityTransferFunction = 'PiecewiseFunction'
tube7Display_1.DataAxesGrid = 'GridAxesRepresentation'
tube7Display_1.PolarAxes = 'PolarAxesRepresentation'
tube7Display_1.SelectInputVectors = ['POINTS', 'Normals']
tube7Display_1.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tube7Display_1.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tube7Display_1.ScaleTransferFunction.Points = [-0.2159722444686844, 0.0, 0.5, 0.0, 0.21612244707438494, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tube7Display_1.OpacityTransferFunction.Points = [-0.2159722444686844, 0.0, 0.5, 0.0, 0.21612244707438494, 1.0, 0.5, 0.0]

# show data from tTKTextureMapFromField1
tTKTextureMapFromField1Display_1 = Show(tTKTextureMapFromField1, renderView6, 'GeometryRepresentation')

# trace defaults for the display properties.
tTKTextureMapFromField1Display_1.Representation = 'Surface'
tTKTextureMapFromField1Display_1.ColorArrayName = ['POINTS', 'y']
tTKTextureMapFromField1Display_1.LookupTable = yLUT
tTKTextureMapFromField1Display_1.Specular = 1.0
tTKTextureMapFromField1Display_1.SelectTCoordArray = 'UV coordinates from field'
tTKTextureMapFromField1Display_1.SelectNormalArray = 'None'
tTKTextureMapFromField1Display_1.SelectTangentArray = 'None'
tTKTextureMapFromField1Display_1.EdgeColor = [0.0, 0.0, 0.0]
tTKTextureMapFromField1Display_1.OSPRayScaleArray = 'y'
tTKTextureMapFromField1Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
tTKTextureMapFromField1Display_1.SelectOrientationVectors = 'Bz'
tTKTextureMapFromField1Display_1.ScaleFactor = 1.0061825752258302
tTKTextureMapFromField1Display_1.SelectScaleArray = 'y'
tTKTextureMapFromField1Display_1.GlyphType = 'Arrow'
tTKTextureMapFromField1Display_1.GlyphTableIndexArray = 'y'
tTKTextureMapFromField1Display_1.GaussianRadius = 0.050309128761291504
tTKTextureMapFromField1Display_1.SetScaleArray = ['POINTS', 'y']
tTKTextureMapFromField1Display_1.ScaleTransferFunction = 'PiecewiseFunction'
tTKTextureMapFromField1Display_1.OpacityArray = ['POINTS', 'y']
tTKTextureMapFromField1Display_1.OpacityTransferFunction = 'PiecewiseFunction'
tTKTextureMapFromField1Display_1.DataAxesGrid = 'GridAxesRepresentation'
tTKTextureMapFromField1Display_1.PolarAxes = 'PolarAxesRepresentation'
tTKTextureMapFromField1Display_1.SelectInputVectors = ['POINTS', 'Bz']
tTKTextureMapFromField1Display_1.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKTextureMapFromField1Display_1.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKTextureMapFromField1Display_1.ScaleTransferFunction.Points = [-4.233413219451904, 0.0, 0.5, 0.0, 4.233413219451904, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKTextureMapFromField1Display_1.OpacityTransferFunction.Points = [-4.233413219451904, 0.0, 0.5, 0.0, 4.233413219451904, 1.0, 0.5, 0.0]

# hide data in view
Hide(contour1, renderView6)

# hide data in view
Hide(connectivity1, renderView6)

# hide data in view
Hide(contour2, renderView6)

# hide data in view
Hide(connectivity2, renderView6)

# hide data in view
Hide(contour3, renderView6)

# hide data in view
Hide(connectivity3, renderView6)

# hide data in view
Hide(tube7, renderView6)

# hide data in view
Hide(tTKTextureMapFromField1, renderView6)

# ----------------------------------------------------------------
# setup the visualization in view 'renderView7'
# ----------------------------------------------------------------

# show data from start_data_omega_bzvti
start_data_omega_bzvtiDisplay_7 = Show(start_data_omega_bzvti, renderView7, 'UniformGridRepresentation')

# trace defaults for the display properties.
start_data_omega_bzvtiDisplay_7.Representation = 'Outline'
start_data_omega_bzvtiDisplay_7.AmbientColor = [0.1803921568627451, 0.17647058823529413, 0.17647058823529413]
start_data_omega_bzvtiDisplay_7.ColorArrayName = ['POINTS', '']
start_data_omega_bzvtiDisplay_7.DiffuseColor = [0.1803921568627451, 0.17647058823529413, 0.17647058823529413]
start_data_omega_bzvtiDisplay_7.SelectTCoordArray = 'None'
start_data_omega_bzvtiDisplay_7.SelectNormalArray = 'None'
start_data_omega_bzvtiDisplay_7.SelectTangentArray = 'None'
start_data_omega_bzvtiDisplay_7.OSPRayScaleArray = 'bz_wz'
start_data_omega_bzvtiDisplay_7.OSPRayScaleFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay_7.SelectOrientationVectors = 'None'
start_data_omega_bzvtiDisplay_7.ScaleFactor = 1.006182531816462
start_data_omega_bzvtiDisplay_7.SelectScaleArray = 'None'
start_data_omega_bzvtiDisplay_7.GlyphType = 'Arrow'
start_data_omega_bzvtiDisplay_7.GlyphTableIndexArray = 'None'
start_data_omega_bzvtiDisplay_7.GaussianRadius = 0.050309126590823094
start_data_omega_bzvtiDisplay_7.SetScaleArray = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_7.ScaleTransferFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay_7.OpacityArray = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_7.OpacityTransferFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay_7.DataAxesGrid = 'GridAxesRepresentation'
start_data_omega_bzvtiDisplay_7.PolarAxes = 'PolarAxesRepresentation'
start_data_omega_bzvtiDisplay_7.ScalarOpacityUnitDistance = 0.12315087617612483
start_data_omega_bzvtiDisplay_7.OpacityArrayName = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_7.SliceFunction = 'Plane'
start_data_omega_bzvtiDisplay_7.Slice = 63
start_data_omega_bzvtiDisplay_7.SelectInputVectors = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_7.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
start_data_omega_bzvtiDisplay_7.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
start_data_omega_bzvtiDisplay_7.ScaleTransferFunction.Points = [-0.7038620845610734, 0.0, 0.5, 0.0, 9.253598515594783, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
start_data_omega_bzvtiDisplay_7.OpacityTransferFunction.Points = [-0.7038620845610734, 0.0, 0.5, 0.0, 9.253598515594783, 1.0, 0.5, 0.0]

# show data from threshold5
threshold5Display = Show(threshold5, renderView7, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
threshold5Display.Representation = 'Surface'
threshold5Display.ColorArrayName = ['POINTS', 'bz_wz']
threshold5Display.LookupTable = bz_wzLUT
threshold5Display.Opacity = 0.3
threshold5Display.Specular = 1.0
threshold5Display.SelectTCoordArray = 'None'
threshold5Display.SelectNormalArray = 'Normals'
threshold5Display.SelectTangentArray = 'None'
threshold5Display.OSPRayScaleArray = 'RegionId'
threshold5Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold5Display.SelectOrientationVectors = 'None'
threshold5Display.ScaleFactor = 0.846682643890381
threshold5Display.SelectScaleArray = 'RegionId'
threshold5Display.GlyphType = 'Arrow'
threshold5Display.GlyphTableIndexArray = 'RegionId'
threshold5Display.GaussianRadius = 0.04233413219451904
threshold5Display.SetScaleArray = ['POINTS', 'RegionId']
threshold5Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold5Display.OpacityArray = ['POINTS', 'RegionId']
threshold5Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold5Display.DataAxesGrid = 'GridAxesRepresentation'
threshold5Display.PolarAxes = 'PolarAxesRepresentation'
threshold5Display.ScalarOpacityFunction = bz_wzPWF
threshold5Display.ScalarOpacityUnitDistance = 0.2873884165867302
threshold5Display.OpacityArrayName = ['POINTS', 'RegionId']
threshold5Display.SelectInputVectors = ['POINTS', 'Normals']
threshold5Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
threshold5Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold5Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold5Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# show data from threshold8
threshold8Display = Show(threshold8, renderView7, 'UnstructuredGridRepresentation')

# get opacity transfer function/opacity map for 'RegionId'
regionIdPWF = GetOpacityTransferFunction('RegionId')
regionIdPWF.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]
regionIdPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
threshold8Display.Representation = 'Surface'
threshold8Display.ColorArrayName = ['POINTS', 'RegionId']
threshold8Display.LookupTable = regionIdLUT
threshold8Display.Opacity = 0.3
threshold8Display.Specular = 1.0
threshold8Display.SelectTCoordArray = 'None'
threshold8Display.SelectNormalArray = 'Normals'
threshold8Display.SelectTangentArray = 'None'
threshold8Display.OSPRayScaleArray = 'RegionId'
threshold8Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold8Display.SelectOrientationVectors = 'None'
threshold8Display.ScaleFactor = 0.846682643890381
threshold8Display.SelectScaleArray = 'RegionId'
threshold8Display.GlyphType = 'Arrow'
threshold8Display.GlyphTableIndexArray = 'RegionId'
threshold8Display.GaussianRadius = 0.04233413219451904
threshold8Display.SetScaleArray = ['POINTS', 'RegionId']
threshold8Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold8Display.OpacityArray = ['POINTS', 'RegionId']
threshold8Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold8Display.DataAxesGrid = 'GridAxesRepresentation'
threshold8Display.PolarAxes = 'PolarAxesRepresentation'
threshold8Display.ScalarOpacityFunction = regionIdPWF
threshold8Display.ScalarOpacityUnitDistance = 0.3316778671322185
threshold8Display.OpacityArrayName = ['POINTS', 'RegionId']
threshold8Display.SelectInputVectors = ['POINTS', 'Normals']
threshold8Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
threshold8Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold8Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold8Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# show data from contour4
contour4Display = Show(contour4, renderView7, 'GeometryRepresentation')

# trace defaults for the display properties.
contour4Display.Representation = 'Surface'
contour4Display.ColorArrayName = ['POINTS', 'bz_wz']
contour4Display.LookupTable = bz_wzLUT
contour4Display.Specular = 1.0
contour4Display.SelectTCoordArray = 'None'
contour4Display.SelectNormalArray = 'Normals'
contour4Display.SelectTangentArray = 'None'
contour4Display.EdgeColor = [0.0, 0.0, 0.0]
contour4Display.OSPRayScaleArray = 'omega_bz'
contour4Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour4Display.SelectOrientationVectors = 'None'
contour4Display.ScaleFactor = 0.846682643890381
contour4Display.SelectScaleArray = 'omega_bz'
contour4Display.GlyphType = 'Arrow'
contour4Display.GlyphTableIndexArray = 'omega_bz'
contour4Display.GaussianRadius = 0.04233413219451904
contour4Display.SetScaleArray = ['POINTS', 'omega_bz']
contour4Display.ScaleTransferFunction = 'PiecewiseFunction'
contour4Display.OpacityArray = ['POINTS', 'omega_bz']
contour4Display.OpacityTransferFunction = 'PiecewiseFunction'
contour4Display.DataAxesGrid = 'GridAxesRepresentation'
contour4Display.PolarAxes = 'PolarAxesRepresentation'
contour4Display.SelectInputVectors = ['POINTS', 'Normals']
contour4Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
contour4Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour4Display.ScaleTransferFunction.Points = [0.9900000095367432, 0.0, 0.5, 0.0, 0.9901220798492432, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour4Display.OpacityTransferFunction.Points = [0.9900000095367432, 0.0, 0.5, 0.0, 0.9901220798492432, 1.0, 0.5, 0.0]

# hide data in view
Hide(start_data_omega_bzvti, renderView7)

# ----------------------------------------------------------------
# setup the visualization in view 'renderView8'
# ----------------------------------------------------------------

# show data from start_data_omega_bzvti
start_data_omega_bzvtiDisplay_8 = Show(start_data_omega_bzvti, renderView8, 'UniformGridRepresentation')

# trace defaults for the display properties.
start_data_omega_bzvtiDisplay_8.Representation = 'Outline'
start_data_omega_bzvtiDisplay_8.AmbientColor = [0.1803921568627451, 0.17647058823529413, 0.17647058823529413]
start_data_omega_bzvtiDisplay_8.ColorArrayName = ['POINTS', '']
start_data_omega_bzvtiDisplay_8.DiffuseColor = [0.1803921568627451, 0.17647058823529413, 0.17647058823529413]
start_data_omega_bzvtiDisplay_8.SelectTCoordArray = 'None'
start_data_omega_bzvtiDisplay_8.SelectNormalArray = 'None'
start_data_omega_bzvtiDisplay_8.SelectTangentArray = 'None'
start_data_omega_bzvtiDisplay_8.OSPRayScaleArray = 'bz_wz'
start_data_omega_bzvtiDisplay_8.OSPRayScaleFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay_8.SelectOrientationVectors = 'None'
start_data_omega_bzvtiDisplay_8.ScaleFactor = 1.006182531816462
start_data_omega_bzvtiDisplay_8.SelectScaleArray = 'None'
start_data_omega_bzvtiDisplay_8.GlyphType = 'Arrow'
start_data_omega_bzvtiDisplay_8.GlyphTableIndexArray = 'None'
start_data_omega_bzvtiDisplay_8.GaussianRadius = 0.050309126590823094
start_data_omega_bzvtiDisplay_8.SetScaleArray = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_8.ScaleTransferFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay_8.OpacityArray = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_8.OpacityTransferFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay_8.DataAxesGrid = 'GridAxesRepresentation'
start_data_omega_bzvtiDisplay_8.PolarAxes = 'PolarAxesRepresentation'
start_data_omega_bzvtiDisplay_8.ScalarOpacityUnitDistance = 0.12315087617612483
start_data_omega_bzvtiDisplay_8.OpacityArrayName = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_8.SliceFunction = 'Plane'
start_data_omega_bzvtiDisplay_8.Slice = 63
start_data_omega_bzvtiDisplay_8.SelectInputVectors = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_8.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
start_data_omega_bzvtiDisplay_8.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
start_data_omega_bzvtiDisplay_8.ScaleTransferFunction.Points = [-0.7038620845610734, 0.0, 0.5, 0.0, 9.253598515594783, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
start_data_omega_bzvtiDisplay_8.OpacityTransferFunction.Points = [-0.7038620845610734, 0.0, 0.5, 0.0, 9.253598515594783, 1.0, 0.5, 0.0]

# show data from contour1
contour1Display_8 = Show(contour1, renderView8, 'GeometryRepresentation')

# trace defaults for the display properties.
contour1Display_8.Representation = 'Surface'
contour1Display_8.ColorArrayName = ['POINTS', '']
contour1Display_8.LookupTable = omega_bzLUT
contour1Display_8.Opacity = 0.2
contour1Display_8.Specular = 1.0
contour1Display_8.SelectTCoordArray = 'None'
contour1Display_8.SelectNormalArray = 'Normals'
contour1Display_8.SelectTangentArray = 'None'
contour1Display_8.EdgeColor = [0.0, 0.0, 0.0]
contour1Display_8.OSPRayScaleArray = 'omega_bz'
contour1Display_8.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display_8.SelectOrientationVectors = 'None'
contour1Display_8.ScaleFactor = 0.8636709690093994
contour1Display_8.SelectScaleArray = 'omega_bz'
contour1Display_8.GlyphType = 'Arrow'
contour1Display_8.GlyphTableIndexArray = 'omega_bz'
contour1Display_8.GaussianRadius = 0.04318354845046997
contour1Display_8.SetScaleArray = ['POINTS', 'omega_bz']
contour1Display_8.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display_8.OpacityArray = ['POINTS', 'omega_bz']
contour1Display_8.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display_8.DataAxesGrid = 'GridAxesRepresentation'
contour1Display_8.PolarAxes = 'PolarAxesRepresentation'
contour1Display_8.SelectInputVectors = ['POINTS', 'Normals']
contour1Display_8.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
contour1Display_8.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour1Display_8.ScaleTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5001220703125, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour1Display_8.OpacityTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5001220703125, 1.0, 0.5, 0.0]

# show data from tTKDiscreteGradient1
tTKDiscreteGradient1Display = Show(tTKDiscreteGradient1, renderView8, 'GeometryRepresentation')

# trace defaults for the display properties.
tTKDiscreteGradient1Display.Representation = 'Surface'
tTKDiscreteGradient1Display.ColorArrayName = ['POINTS', 'CellDimension']
tTKDiscreteGradient1Display.LookupTable = cellDimensionLUT
tTKDiscreteGradient1Display.Specular = 1.0
tTKDiscreteGradient1Display.SelectTCoordArray = 'None'
tTKDiscreteGradient1Display.SelectNormalArray = 'None'
tTKDiscreteGradient1Display.SelectTangentArray = 'None'
tTKDiscreteGradient1Display.EdgeColor = [0.0, 0.0, 0.0]
tTKDiscreteGradient1Display.OSPRayScaleArray = 'CellDimension'
tTKDiscreteGradient1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKDiscreteGradient1Display.SelectOrientationVectors = 'None'
tTKDiscreteGradient1Display.ScaleFactor = 0.8466827392578126
tTKDiscreteGradient1Display.SelectScaleArray = 'CellDimension'
tTKDiscreteGradient1Display.GlyphType = 'Arrow'
tTKDiscreteGradient1Display.GlyphTableIndexArray = 'CellDimension'
tTKDiscreteGradient1Display.GaussianRadius = 0.04233413696289062
tTKDiscreteGradient1Display.SetScaleArray = ['POINTS', 'CellDimension']
tTKDiscreteGradient1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKDiscreteGradient1Display.OpacityArray = ['POINTS', 'CellDimension']
tTKDiscreteGradient1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKDiscreteGradient1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKDiscreteGradient1Display.PolarAxes = 'PolarAxesRepresentation'
tTKDiscreteGradient1Display.SelectInputVectors = ['POINTS', 'CellDimension']
tTKDiscreteGradient1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKDiscreteGradient1Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKDiscreteGradient1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKDiscreteGradient1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# find source
tTKDiscreteGradient1_1 = FindSource('TTKDiscreteGradient1')

# show data from tTKDiscreteGradient1_1
tTKDiscreteGradient1_1Display = Show(OutputPort(tTKDiscreteGradient1_1, 1), renderView8, 'GeometryRepresentation')

# trace defaults for the display properties.
tTKDiscreteGradient1_1Display.Representation = 'Surface'
tTKDiscreteGradient1_1Display.ColorArrayName = ['POINTS', '']
tTKDiscreteGradient1_1Display.Specular = 1.0
tTKDiscreteGradient1_1Display.SelectTCoordArray = 'None'
tTKDiscreteGradient1_1Display.SelectNormalArray = 'None'
tTKDiscreteGradient1_1Display.SelectTangentArray = 'None'
tTKDiscreteGradient1_1Display.EdgeColor = [0.0, 0.0, 0.0]
tTKDiscreteGradient1_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKDiscreteGradient1_1Display.SelectOrientationVectors = 'None'
tTKDiscreteGradient1_1Display.ScaleFactor = -0.2
tTKDiscreteGradient1_1Display.SelectScaleArray = 'None'
tTKDiscreteGradient1_1Display.GlyphType = 'Arrow'
tTKDiscreteGradient1_1Display.GlyphTableIndexArray = 'None'
tTKDiscreteGradient1_1Display.GaussianRadius = -0.01
tTKDiscreteGradient1_1Display.SetScaleArray = ['POINTS', '']
tTKDiscreteGradient1_1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKDiscreteGradient1_1Display.OpacityArray = ['POINTS', '']
tTKDiscreteGradient1_1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKDiscreteGradient1_1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKDiscreteGradient1_1Display.PolarAxes = 'PolarAxesRepresentation'
tTKDiscreteGradient1_1Display.SelectInputVectors = ['POINTS', '']
tTKDiscreteGradient1_1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKDiscreteGradient1_1Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# show data from tTKIcospheresFromPoints1
tTKIcospheresFromPoints1Display = Show(tTKIcospheresFromPoints1, renderView8, 'GeometryRepresentation')

# trace defaults for the display properties.
tTKIcospheresFromPoints1Display.Representation = 'Surface'
tTKIcospheresFromPoints1Display.ColorArrayName = ['POINTS', 'CellDimension']
tTKIcospheresFromPoints1Display.LookupTable = cellDimensionLUT
tTKIcospheresFromPoints1Display.Specular = 1.0
tTKIcospheresFromPoints1Display.SelectTCoordArray = 'None'
tTKIcospheresFromPoints1Display.SelectNormalArray = 'Normals'
tTKIcospheresFromPoints1Display.SelectTangentArray = 'None'
tTKIcospheresFromPoints1Display.EdgeColor = [0.0, 0.0, 0.0]
tTKIcospheresFromPoints1Display.OSPRayScaleArray = 'CellDimension'
tTKIcospheresFromPoints1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKIcospheresFromPoints1Display.SelectOrientationVectors = 'None'
tTKIcospheresFromPoints1Display.ScaleFactor = 1.0466827392578126
tTKIcospheresFromPoints1Display.SelectScaleArray = 'CellDimension'
tTKIcospheresFromPoints1Display.GlyphType = 'Arrow'
tTKIcospheresFromPoints1Display.GlyphTableIndexArray = 'CellDimension'
tTKIcospheresFromPoints1Display.GaussianRadius = 0.052334136962890625
tTKIcospheresFromPoints1Display.SetScaleArray = ['POINTS', 'CellDimension']
tTKIcospheresFromPoints1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKIcospheresFromPoints1Display.OpacityArray = ['POINTS', 'CellDimension']
tTKIcospheresFromPoints1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKIcospheresFromPoints1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKIcospheresFromPoints1Display.PolarAxes = 'PolarAxesRepresentation'
tTKIcospheresFromPoints1Display.SelectInputVectors = ['POINTS', 'CellDimension']
tTKIcospheresFromPoints1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKIcospheresFromPoints1Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKIcospheresFromPoints1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKIcospheresFromPoints1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# show data from extractSurface1
extractSurface1Display = Show(extractSurface1, renderView8, 'GeometryRepresentation')

# trace defaults for the display properties.
extractSurface1Display.Representation = 'Surface'
extractSurface1Display.ColorArrayName = ['CELLS', 'SeparatrixType']
extractSurface1Display.LookupTable = separatrixTypeLUT
extractSurface1Display.Specular = 1.0
extractSurface1Display.SelectTCoordArray = 'None'
extractSurface1Display.SelectNormalArray = 'None'
extractSurface1Display.SelectTangentArray = 'None'
extractSurface1Display.EdgeColor = [0.0, 0.0, 0.0]
extractSurface1Display.OSPRayScaleArray = 'CellDimension'
extractSurface1Display.OSPRayScaleFunction = 'PiecewiseFunction'
extractSurface1Display.SelectOrientationVectors = 'None'
extractSurface1Display.ScaleFactor = 0.8466827869415283
extractSurface1Display.SelectScaleArray = 'SeparatrixType'
extractSurface1Display.GlyphType = 'Arrow'
extractSurface1Display.GlyphTableIndexArray = 'SeparatrixType'
extractSurface1Display.GaussianRadius = 0.042334139347076416
extractSurface1Display.SetScaleArray = ['POINTS', 'CellDimension']
extractSurface1Display.ScaleTransferFunction = 'PiecewiseFunction'
extractSurface1Display.OpacityArray = ['POINTS', 'CellDimension']
extractSurface1Display.OpacityTransferFunction = 'PiecewiseFunction'
extractSurface1Display.DataAxesGrid = 'GridAxesRepresentation'
extractSurface1Display.PolarAxes = 'PolarAxesRepresentation'
extractSurface1Display.SelectInputVectors = ['POINTS', 'CellDimension']
extractSurface1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
extractSurface1Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
extractSurface1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
extractSurface1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# hide data in view
Hide(extractSurface1, renderView8)

# ----------------------------------------------------------------
# setup the visualization in view 'renderView9'
# ----------------------------------------------------------------

# show data from tTKScalarFieldNormalizer1
tTKScalarFieldNormalizer1Display = Show(tTKScalarFieldNormalizer1, renderView9, 'UniformGridRepresentation')

# trace defaults for the display properties.
tTKScalarFieldNormalizer1Display.Representation = 'Outline'
tTKScalarFieldNormalizer1Display.ColorArrayName = ['POINTS', '']
tTKScalarFieldNormalizer1Display.SelectTCoordArray = 'None'
tTKScalarFieldNormalizer1Display.SelectNormalArray = 'None'
tTKScalarFieldNormalizer1Display.SelectTangentArray = 'None'
tTKScalarFieldNormalizer1Display.OSPRayScaleArray = 'bz_wz'
tTKScalarFieldNormalizer1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKScalarFieldNormalizer1Display.SelectOrientationVectors = 'None'
tTKScalarFieldNormalizer1Display.ScaleFactor = 1.006182531816462
tTKScalarFieldNormalizer1Display.SelectScaleArray = 'None'
tTKScalarFieldNormalizer1Display.GlyphType = 'Arrow'
tTKScalarFieldNormalizer1Display.GlyphTableIndexArray = 'None'
tTKScalarFieldNormalizer1Display.GaussianRadius = 0.050309126590823094
tTKScalarFieldNormalizer1Display.SetScaleArray = ['POINTS', 'bz_wz']
tTKScalarFieldNormalizer1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKScalarFieldNormalizer1Display.OpacityArray = ['POINTS', 'bz_wz']
tTKScalarFieldNormalizer1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKScalarFieldNormalizer1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKScalarFieldNormalizer1Display.PolarAxes = 'PolarAxesRepresentation'
tTKScalarFieldNormalizer1Display.ScalarOpacityUnitDistance = 0.12315087617612483
tTKScalarFieldNormalizer1Display.OpacityArrayName = ['POINTS', 'bz_wz']
tTKScalarFieldNormalizer1Display.SliceFunction = 'Plane'
tTKScalarFieldNormalizer1Display.Slice = 63
tTKScalarFieldNormalizer1Display.SelectInputVectors = ['POINTS', 'bz_wz']
tTKScalarFieldNormalizer1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKScalarFieldNormalizer1Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKScalarFieldNormalizer1Display.ScaleTransferFunction.Points = [-0.7038620845610734, 0.0, 0.5, 0.0, 9.253598515594783, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKScalarFieldNormalizer1Display.OpacityTransferFunction.Points = [-0.7038620845610734, 0.0, 0.5, 0.0, 9.253598515594783, 1.0, 0.5, 0.0]

# show data from tTKPersistenceDiagram1
tTKPersistenceDiagram1Display = Show(tTKPersistenceDiagram1, renderView9, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
tTKPersistenceDiagram1Display.Representation = 'Surface'
tTKPersistenceDiagram1Display.AmbientColor = [0.6666666666666666, 0.21176470588235294, 0.19607843137254902]
tTKPersistenceDiagram1Display.ColorArrayName = ['POINTS', '']
tTKPersistenceDiagram1Display.DiffuseColor = [0.6666666666666666, 0.21176470588235294, 0.19607843137254902]
tTKPersistenceDiagram1Display.Specular = 1.0
tTKPersistenceDiagram1Display.SelectTCoordArray = 'None'
tTKPersistenceDiagram1Display.SelectNormalArray = 'None'
tTKPersistenceDiagram1Display.SelectTangentArray = 'None'
tTKPersistenceDiagram1Display.OSPRayScaleArray = 'Coordinates'
tTKPersistenceDiagram1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKPersistenceDiagram1Display.SelectOrientationVectors = 'Coordinates'
tTKPersistenceDiagram1Display.ScaleFactor = 0.0999999953674319
tTKPersistenceDiagram1Display.SelectScaleArray = 'Coordinates'
tTKPersistenceDiagram1Display.GlyphType = 'Arrow'
tTKPersistenceDiagram1Display.GlyphTableIndexArray = 'Coordinates'
tTKPersistenceDiagram1Display.GaussianRadius = 0.004999999768371594
tTKPersistenceDiagram1Display.SetScaleArray = ['POINTS', 'Coordinates']
tTKPersistenceDiagram1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKPersistenceDiagram1Display.OpacityArray = ['POINTS', 'Coordinates']
tTKPersistenceDiagram1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKPersistenceDiagram1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKPersistenceDiagram1Display.PolarAxes = 'PolarAxesRepresentation'
tTKPersistenceDiagram1Display.ScalarOpacityUnitDistance = 0.2181304645116989
tTKPersistenceDiagram1Display.OpacityArrayName = ['POINTS', 'Coordinates']
tTKPersistenceDiagram1Display.SelectInputVectors = ['POINTS', 'Coordinates']
tTKPersistenceDiagram1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKPersistenceDiagram1Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKPersistenceDiagram1Display.ScaleTransferFunction.Points = [-2.4164228439331055, 0.0, 0.5, 0.0, 5.030911922454834, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKPersistenceDiagram1Display.OpacityTransferFunction.Points = [-2.4164228439331055, 0.0, 0.5, 0.0, 5.030911922454834, 1.0, 0.5, 0.0]

# show data from threshold9
threshold9Display = Show(threshold9, renderView9, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'Coordinates'
coordinatesLUT = GetColorTransferFunction('Coordinates')
coordinatesLUT.RGBPoints = [0.06157508338376992, 0.0, 0.129412, 0.584314, 3.3183771414326744, 0.917647, 0.941176, 0.788235, 6.575179199481572, 0.0, 0.431373, 0.0]
coordinatesLUT.ColorSpace = 'RGB'
coordinatesLUT.AboveRangeColor = [1.0, 1.0, 1.0]
coordinatesLUT.NanColor = [0.0, 0.0, 0.0]
coordinatesLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'Coordinates'
coordinatesPWF = GetOpacityTransferFunction('Coordinates')
coordinatesPWF.Points = [0.06157508338376992, 0.0, 0.5, 0.0, 6.575179199481572, 1.0, 0.5, 0.0]
coordinatesPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
threshold9Display.Representation = 'Surface'
threshold9Display.ColorArrayName = ['POINTS', 'Coordinates']
threshold9Display.LookupTable = coordinatesLUT
threshold9Display.Specular = 1.0
threshold9Display.SelectTCoordArray = 'None'
threshold9Display.SelectNormalArray = 'None'
threshold9Display.SelectTangentArray = 'None'
threshold9Display.OSPRayScaleArray = 'Coordinates'
threshold9Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold9Display.SelectOrientationVectors = 'Coordinates'
threshold9Display.ScaleFactor = 0.09987303747406032
threshold9Display.SelectScaleArray = 'Coordinates'
threshold9Display.GlyphType = 'Arrow'
threshold9Display.GlyphTableIndexArray = 'Coordinates'
threshold9Display.GaussianRadius = 0.004993651873703015
threshold9Display.SetScaleArray = ['POINTS', 'Coordinates']
threshold9Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold9Display.OpacityArray = ['POINTS', 'Coordinates']
threshold9Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold9Display.DataAxesGrid = 'GridAxesRepresentation'
threshold9Display.PolarAxes = 'PolarAxesRepresentation'
threshold9Display.ScalarOpacityFunction = coordinatesPWF
threshold9Display.ScalarOpacityUnitDistance = 1.4124180411121245
threshold9Display.OpacityArrayName = ['POINTS', 'Coordinates']
threshold9Display.SelectInputVectors = ['POINTS', 'Coordinates']
threshold9Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
threshold9Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold9Display.ScaleTransferFunction.Points = [-1.386472225189209, 0.0, 0.5, 0.0, 4.080188274383545, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold9Display.OpacityTransferFunction.Points = [-1.386472225189209, 0.0, 0.5, 0.0, 4.080188274383545, 1.0, 0.5, 0.0]

# show data from extractSurface2
extractSurface2Display = Show(extractSurface2, renderView9, 'GeometryRepresentation')

# trace defaults for the display properties.
extractSurface2Display.Representation = 'Surface'
extractSurface2Display.ColorArrayName = ['POINTS', 'Coordinates']
extractSurface2Display.LookupTable = coordinatesLUT
extractSurface2Display.Specular = 1.0
extractSurface2Display.SelectTCoordArray = 'None'
extractSurface2Display.SelectNormalArray = 'None'
extractSurface2Display.SelectTangentArray = 'None'
extractSurface2Display.EdgeColor = [0.0, 0.0, 0.0]
extractSurface2Display.OSPRayScaleArray = 'Coordinates'
extractSurface2Display.OSPRayScaleFunction = 'PiecewiseFunction'
extractSurface2Display.SelectOrientationVectors = 'Coordinates'
extractSurface2Display.ScaleFactor = 0.09987303747406032
extractSurface2Display.SelectScaleArray = 'Coordinates'
extractSurface2Display.GlyphType = 'Arrow'
extractSurface2Display.GlyphTableIndexArray = 'Coordinates'
extractSurface2Display.GaussianRadius = 0.004993651873703015
extractSurface2Display.SetScaleArray = ['POINTS', 'Coordinates']
extractSurface2Display.ScaleTransferFunction = 'PiecewiseFunction'
extractSurface2Display.OpacityArray = ['POINTS', 'Coordinates']
extractSurface2Display.OpacityTransferFunction = 'PiecewiseFunction'
extractSurface2Display.DataAxesGrid = 'GridAxesRepresentation'
extractSurface2Display.PolarAxes = 'PolarAxesRepresentation'
extractSurface2Display.SelectInputVectors = ['POINTS', 'Coordinates']
extractSurface2Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
extractSurface2Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
extractSurface2Display.ScaleTransferFunction.Points = [-1.386472225189209, 0.0, 0.5, 0.0, 4.080188274383545, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
extractSurface2Display.OpacityTransferFunction.Points = [-1.386472225189209, 0.0, 0.5, 0.0, 4.080188274383545, 1.0, 0.5, 0.0]

# show data from tube2
tube2Display = Show(tube2, renderView9, 'GeometryRepresentation')

# trace defaults for the display properties.
tube2Display.Representation = 'Surface'
tube2Display.AmbientColor = [0.1803921568627451, 0.17647058823529413, 0.17647058823529413]
tube2Display.ColorArrayName = ['POINTS', '']
tube2Display.DiffuseColor = [0.1803921568627451, 0.17647058823529413, 0.17647058823529413]
tube2Display.LookupTable = coordinatesLUT
tube2Display.Specular = 1.0
tube2Display.SelectTCoordArray = 'None'
tube2Display.SelectNormalArray = 'TubeNormals'
tube2Display.SelectTangentArray = 'None'
tube2Display.EdgeColor = [0.0, 0.0, 0.0]
tube2Display.OSPRayScaleArray = 'Coordinates'
tube2Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube2Display.SelectOrientationVectors = 'Coordinates'
tube2Display.ScaleFactor = 0.10109622376039624
tube2Display.SelectScaleArray = 'Coordinates'
tube2Display.GlyphType = 'Arrow'
tube2Display.GlyphTableIndexArray = 'Coordinates'
tube2Display.GaussianRadius = 0.005054811188019813
tube2Display.SetScaleArray = ['POINTS', 'Coordinates']
tube2Display.ScaleTransferFunction = 'PiecewiseFunction'
tube2Display.OpacityArray = ['POINTS', 'Coordinates']
tube2Display.OpacityTransferFunction = 'PiecewiseFunction'
tube2Display.DataAxesGrid = 'GridAxesRepresentation'
tube2Display.PolarAxes = 'PolarAxesRepresentation'
tube2Display.SelectInputVectors = ['POINTS', 'Coordinates']
tube2Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tube2Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tube2Display.ScaleTransferFunction.Points = [-1.386472225189209, 0.0, 0.5, 0.0, 4.080188274383545, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tube2Display.OpacityTransferFunction.Points = [-1.386472225189209, 0.0, 0.5, 0.0, 4.080188274383545, 1.0, 0.5, 0.0]

# show data from threshold10
threshold10Display = Show(threshold10, renderView9, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
threshold10Display.Representation = 'Surface'
threshold10Display.AmbientColor = [0.6666666666666666, 0.21176470588235294, 0.19607843137254902]
threshold10Display.ColorArrayName = ['POINTS', '']
threshold10Display.DiffuseColor = [0.6666666666666666, 0.21176470588235294, 0.19607843137254902]
threshold10Display.Specular = 1.0
threshold10Display.SelectTCoordArray = 'None'
threshold10Display.SelectNormalArray = 'None'
threshold10Display.SelectTangentArray = 'None'
threshold10Display.OSPRayScaleArray = 'Coordinates'
threshold10Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold10Display.SelectOrientationVectors = 'Coordinates'
threshold10Display.ScaleFactor = 0.0999999953674319
threshold10Display.SelectScaleArray = 'Coordinates'
threshold10Display.GlyphType = 'Arrow'
threshold10Display.GlyphTableIndexArray = 'Coordinates'
threshold10Display.GaussianRadius = 0.004999999768371594
threshold10Display.SetScaleArray = ['POINTS', 'Coordinates']
threshold10Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold10Display.OpacityArray = ['POINTS', 'Coordinates']
threshold10Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold10Display.DataAxesGrid = 'GridAxesRepresentation'
threshold10Display.PolarAxes = 'PolarAxesRepresentation'
threshold10Display.ScalarOpacityUnitDistance = 0.7388222152624305
threshold10Display.OpacityArrayName = ['POINTS', 'Coordinates']
threshold10Display.SelectInputVectors = ['POINTS', 'Coordinates']
threshold10Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
threshold10Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold10Display.ScaleTransferFunction.Points = [-1.5449261665344238, 0.0, 0.5, 0.0, 4.47632360458374, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold10Display.OpacityTransferFunction.Points = [-1.5449261665344238, 0.0, 0.5, 0.0, 4.47632360458374, 1.0, 0.5, 0.0]

# show data from tTKIcospheresFromPoints3
tTKIcospheresFromPoints3Display = Show(tTKIcospheresFromPoints3, renderView9, 'GeometryRepresentation')

# get color transfer function/color map for 'CriticalType'
criticalTypeLUT = GetColorTransferFunction('CriticalType')
criticalTypeLUT.RGBPoints = [0.0, 0.0, 0.129412, 0.584314, 1.5000000000000013, 0.917647, 0.941176, 0.788235, 3.0, 0.0, 0.431373, 0.0]
criticalTypeLUT.ColorSpace = 'RGB'
criticalTypeLUT.AboveRangeColor = [1.0, 1.0, 1.0]
criticalTypeLUT.NanColor = [0.0, 0.0, 0.0]
criticalTypeLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
tTKIcospheresFromPoints3Display.Representation = 'Surface'
tTKIcospheresFromPoints3Display.ColorArrayName = ['POINTS', 'CriticalType']
tTKIcospheresFromPoints3Display.LookupTable = criticalTypeLUT
tTKIcospheresFromPoints3Display.Specular = 1.0
tTKIcospheresFromPoints3Display.SelectTCoordArray = 'None'
tTKIcospheresFromPoints3Display.SelectNormalArray = 'Normals'
tTKIcospheresFromPoints3Display.SelectTangentArray = 'None'
tTKIcospheresFromPoints3Display.EdgeColor = [0.0, 0.0, 0.0]
tTKIcospheresFromPoints3Display.OSPRayScaleArray = 'Coordinates'
tTKIcospheresFromPoints3Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKIcospheresFromPoints3Display.SelectOrientationVectors = 'Coordinates'
tTKIcospheresFromPoints3Display.ScaleFactor = 0.29999999403953553
tTKIcospheresFromPoints3Display.SelectScaleArray = 'Coordinates'
tTKIcospheresFromPoints3Display.GlyphType = 'Arrow'
tTKIcospheresFromPoints3Display.GlyphTableIndexArray = 'Coordinates'
tTKIcospheresFromPoints3Display.GaussianRadius = 0.014999999701976777
tTKIcospheresFromPoints3Display.SetScaleArray = ['POINTS', 'Coordinates']
tTKIcospheresFromPoints3Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKIcospheresFromPoints3Display.OpacityArray = ['POINTS', 'Coordinates']
tTKIcospheresFromPoints3Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKIcospheresFromPoints3Display.DataAxesGrid = 'GridAxesRepresentation'
tTKIcospheresFromPoints3Display.PolarAxes = 'PolarAxesRepresentation'
tTKIcospheresFromPoints3Display.SelectInputVectors = ['POINTS', 'Coordinates']
tTKIcospheresFromPoints3Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKIcospheresFromPoints3Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKIcospheresFromPoints3Display.ScaleTransferFunction.Points = [-1.5449261665344238, 0.0, 0.5, 0.0, 4.47632360458374, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKIcospheresFromPoints3Display.OpacityTransferFunction.Points = [-1.5449261665344238, 0.0, 0.5, 0.0, 4.47632360458374, 1.0, 0.5, 0.0]

# show data from extractSurface3
extractSurface3Display = Show(extractSurface3, renderView9, 'GeometryRepresentation')

# trace defaults for the display properties.
extractSurface3Display.Representation = 'Surface'
extractSurface3Display.ColorArrayName = ['POINTS', '']
extractSurface3Display.Specular = 1.0
extractSurface3Display.SelectTCoordArray = 'None'
extractSurface3Display.SelectNormalArray = 'None'
extractSurface3Display.SelectTangentArray = 'None'
extractSurface3Display.EdgeColor = [0.0, 0.0, 0.0]
extractSurface3Display.OSPRayScaleArray = 'Coordinates'
extractSurface3Display.OSPRayScaleFunction = 'PiecewiseFunction'
extractSurface3Display.SelectOrientationVectors = 'Coordinates'
extractSurface3Display.ScaleFactor = 0.0999999953674319
extractSurface3Display.SelectScaleArray = 'Coordinates'
extractSurface3Display.GlyphType = 'Arrow'
extractSurface3Display.GlyphTableIndexArray = 'Coordinates'
extractSurface3Display.GaussianRadius = 0.004999999768371594
extractSurface3Display.SetScaleArray = ['POINTS', 'Coordinates']
extractSurface3Display.ScaleTransferFunction = 'PiecewiseFunction'
extractSurface3Display.OpacityArray = ['POINTS', 'Coordinates']
extractSurface3Display.OpacityTransferFunction = 'PiecewiseFunction'
extractSurface3Display.DataAxesGrid = 'GridAxesRepresentation'
extractSurface3Display.PolarAxes = 'PolarAxesRepresentation'
extractSurface3Display.SelectInputVectors = ['POINTS', 'Coordinates']
extractSurface3Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
extractSurface3Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
extractSurface3Display.ScaleTransferFunction.Points = [-1.5449261665344238, 0.0, 0.5, 0.0, 4.47632360458374, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
extractSurface3Display.OpacityTransferFunction.Points = [-1.5449261665344238, 0.0, 0.5, 0.0, 4.47632360458374, 1.0, 0.5, 0.0]

# show data from tube3
tube3Display = Show(tube3, renderView9, 'GeometryRepresentation')

# trace defaults for the display properties.
tube3Display.Representation = 'Surface'
tube3Display.ColorArrayName = ['POINTS', '']
tube3Display.Specular = 1.0
tube3Display.SelectTCoordArray = 'None'
tube3Display.SelectNormalArray = 'TubeNormals'
tube3Display.SelectTangentArray = 'None'
tube3Display.EdgeColor = [0.0, 0.0, 0.0]
tube3Display.OSPRayScaleArray = 'Coordinates'
tube3Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube3Display.SelectOrientationVectors = 'Coordinates'
tube3Display.ScaleFactor = 0.10148541554808617
tube3Display.SelectScaleArray = 'Coordinates'
tube3Display.GlyphType = 'Arrow'
tube3Display.GlyphTableIndexArray = 'Coordinates'
tube3Display.GaussianRadius = 0.005074270777404308
tube3Display.SetScaleArray = ['POINTS', 'Coordinates']
tube3Display.ScaleTransferFunction = 'PiecewiseFunction'
tube3Display.OpacityArray = ['POINTS', 'Coordinates']
tube3Display.OpacityTransferFunction = 'PiecewiseFunction'
tube3Display.DataAxesGrid = 'GridAxesRepresentation'
tube3Display.PolarAxes = 'PolarAxesRepresentation'
tube3Display.SelectInputVectors = ['POINTS', 'Coordinates']
tube3Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tube3Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tube3Display.ScaleTransferFunction.Points = [-1.5449261665344238, 0.0, 0.5, 0.0, 4.47632360458374, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tube3Display.OpacityTransferFunction.Points = [-1.5449261665344238, 0.0, 0.5, 0.0, 4.47632360458374, 1.0, 0.5, 0.0]

# show data from threshold11
threshold11Display = Show(threshold11, renderView9, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
threshold11Display.Representation = 'Surface'
threshold11Display.ColorArrayName = ['POINTS', '']
threshold11Display.Specular = 1.0
threshold11Display.SelectTCoordArray = 'None'
threshold11Display.SelectNormalArray = 'TubeNormals'
threshold11Display.SelectTangentArray = 'None'
threshold11Display.OSPRayScaleArray = 'Coordinates'
threshold11Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold11Display.SelectOrientationVectors = 'Coordinates'
threshold11Display.ScaleFactor = 0.0999999953674319
threshold11Display.SelectScaleArray = 'Coordinates'
threshold11Display.GlyphType = 'Arrow'
threshold11Display.GlyphTableIndexArray = 'Coordinates'
threshold11Display.GaussianRadius = 0.004999999768371594
threshold11Display.SetScaleArray = ['POINTS', 'Coordinates']
threshold11Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold11Display.OpacityArray = ['POINTS', 'Coordinates']
threshold11Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold11Display.DataAxesGrid = 'GridAxesRepresentation'
threshold11Display.PolarAxes = 'PolarAxesRepresentation'
threshold11Display.ScalarOpacityUnitDistance = 0.2965275639969653
threshold11Display.OpacityArrayName = ['POINTS', 'Coordinates']
threshold11Display.SelectInputVectors = ['POINTS', 'Coordinates']
threshold11Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
threshold11Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold11Display.ScaleTransferFunction.Points = [-1.5449261665344238, 0.0, 0.5, 0.0, 4.47632360458374, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold11Display.OpacityTransferFunction.Points = [-1.5449261665344238, 0.0, 0.5, 0.0, 4.47632360458374, 1.0, 0.5, 0.0]

# show data from threshold12
threshold12Display = Show(threshold12, renderView9, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
threshold12Display.Representation = 'Surface'
threshold12Display.ColorArrayName = [None, '']
threshold12Display.Specular = 1.0
threshold12Display.SelectTCoordArray = 'None'
threshold12Display.SelectNormalArray = 'None'
threshold12Display.SelectTangentArray = 'None'
threshold12Display.OSPRayScaleArray = 'Coordinates'
threshold12Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold12Display.SelectOrientationVectors = 'Coordinates'
threshold12Display.ScaleFactor = 0.0999999953674319
threshold12Display.SelectScaleArray = 'Coordinates'
threshold12Display.GlyphType = 'Arrow'
threshold12Display.GlyphTableIndexArray = 'Coordinates'
threshold12Display.GaussianRadius = 0.004999999768371594
threshold12Display.SetScaleArray = ['POINTS', 'Coordinates']
threshold12Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold12Display.OpacityArray = ['POINTS', 'Coordinates']
threshold12Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold12Display.DataAxesGrid = 'GridAxesRepresentation'
threshold12Display.PolarAxes = 'PolarAxesRepresentation'
threshold12Display.ScalarOpacityUnitDistance = 0.2183984383247799
threshold12Display.OpacityArrayName = ['POINTS', 'Coordinates']
threshold12Display.SelectInputVectors = ['POINTS', 'Coordinates']
threshold12Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
threshold12Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold12Display.ScaleTransferFunction.Points = [-2.4164228439331055, 0.0, 0.5, 0.0, 5.030911922454834, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold12Display.OpacityTransferFunction.Points = [-2.4164228439331055, 0.0, 0.5, 0.0, 5.030911922454834, 1.0, 0.5, 0.0]

# show data from tTKIcospheresFromPoints4
tTKIcospheresFromPoints4Display = Show(tTKIcospheresFromPoints4, renderView9, 'GeometryRepresentation')

# trace defaults for the display properties.
tTKIcospheresFromPoints4Display.Representation = 'Surface'
tTKIcospheresFromPoints4Display.ColorArrayName = [None, '']
tTKIcospheresFromPoints4Display.Specular = 1.0
tTKIcospheresFromPoints4Display.SelectTCoordArray = 'None'
tTKIcospheresFromPoints4Display.SelectNormalArray = 'Normals'
tTKIcospheresFromPoints4Display.SelectTangentArray = 'None'
tTKIcospheresFromPoints4Display.EdgeColor = [0.0, 0.0, 0.0]
tTKIcospheresFromPoints4Display.OSPRayScaleArray = 'Coordinates'
tTKIcospheresFromPoints4Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKIcospheresFromPoints4Display.SelectOrientationVectors = 'Coordinates'
tTKIcospheresFromPoints4Display.ScaleFactor = 0.29999999403953553
tTKIcospheresFromPoints4Display.SelectScaleArray = 'Coordinates'
tTKIcospheresFromPoints4Display.GlyphType = 'Arrow'
tTKIcospheresFromPoints4Display.GlyphTableIndexArray = 'Coordinates'
tTKIcospheresFromPoints4Display.GaussianRadius = 0.014999999701976777
tTKIcospheresFromPoints4Display.SetScaleArray = ['POINTS', 'Coordinates']
tTKIcospheresFromPoints4Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKIcospheresFromPoints4Display.OpacityArray = ['POINTS', 'Coordinates']
tTKIcospheresFromPoints4Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKIcospheresFromPoints4Display.DataAxesGrid = 'GridAxesRepresentation'
tTKIcospheresFromPoints4Display.PolarAxes = 'PolarAxesRepresentation'
tTKIcospheresFromPoints4Display.SelectInputVectors = ['POINTS', 'Coordinates']
tTKIcospheresFromPoints4Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKIcospheresFromPoints4Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKIcospheresFromPoints4Display.ScaleTransferFunction.Points = [-2.4164228439331055, 0.0, 0.5, 0.0, 5.030911922454834, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKIcospheresFromPoints4Display.OpacityTransferFunction.Points = [-2.4164228439331055, 0.0, 0.5, 0.0, 5.030911922454834, 1.0, 0.5, 0.0]

# show data from extractSurface4
extractSurface4Display = Show(extractSurface4, renderView9, 'GeometryRepresentation')

# trace defaults for the display properties.
extractSurface4Display.Representation = 'Surface'
extractSurface4Display.ColorArrayName = [None, '']
extractSurface4Display.Specular = 1.0
extractSurface4Display.SelectTCoordArray = 'None'
extractSurface4Display.SelectNormalArray = 'None'
extractSurface4Display.SelectTangentArray = 'None'
extractSurface4Display.EdgeColor = [0.0, 0.0, 0.0]
extractSurface4Display.OSPRayScaleArray = 'Coordinates'
extractSurface4Display.OSPRayScaleFunction = 'PiecewiseFunction'
extractSurface4Display.SelectOrientationVectors = 'Coordinates'
extractSurface4Display.ScaleFactor = 0.0999999953674319
extractSurface4Display.SelectScaleArray = 'Coordinates'
extractSurface4Display.GlyphType = 'Arrow'
extractSurface4Display.GlyphTableIndexArray = 'Coordinates'
extractSurface4Display.GaussianRadius = 0.004999999768371594
extractSurface4Display.SetScaleArray = ['POINTS', 'Coordinates']
extractSurface4Display.ScaleTransferFunction = 'PiecewiseFunction'
extractSurface4Display.OpacityArray = ['POINTS', 'Coordinates']
extractSurface4Display.OpacityTransferFunction = 'PiecewiseFunction'
extractSurface4Display.DataAxesGrid = 'GridAxesRepresentation'
extractSurface4Display.PolarAxes = 'PolarAxesRepresentation'
extractSurface4Display.SelectInputVectors = ['POINTS', 'Coordinates']
extractSurface4Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
extractSurface4Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
extractSurface4Display.ScaleTransferFunction.Points = [-2.4164228439331055, 0.0, 0.5, 0.0, 5.030911922454834, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
extractSurface4Display.OpacityTransferFunction.Points = [-2.4164228439331055, 0.0, 0.5, 0.0, 5.030911922454834, 1.0, 0.5, 0.0]

# show data from tube8
tube8Display = Show(tube8, renderView9, 'GeometryRepresentation')

# trace defaults for the display properties.
tube8Display.Representation = 'Surface'
tube8Display.ColorArrayName = [None, '']
tube8Display.Specular = 1.0
tube8Display.SelectTCoordArray = 'None'
tube8Display.SelectNormalArray = 'TubeNormals'
tube8Display.SelectTangentArray = 'None'
tube8Display.EdgeColor = [0.0, 0.0, 0.0]
tube8Display.OSPRayScaleArray = 'Coordinates'
tube8Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube8Display.SelectOrientationVectors = 'Coordinates'
tube8Display.ScaleFactor = 0.10187303647398949
tube8Display.SelectScaleArray = 'Coordinates'
tube8Display.GlyphType = 'Arrow'
tube8Display.GlyphTableIndexArray = 'Coordinates'
tube8Display.GaussianRadius = 0.005093651823699474
tube8Display.SetScaleArray = ['POINTS', 'Coordinates']
tube8Display.ScaleTransferFunction = 'PiecewiseFunction'
tube8Display.OpacityArray = ['POINTS', 'Coordinates']
tube8Display.OpacityTransferFunction = 'PiecewiseFunction'
tube8Display.DataAxesGrid = 'GridAxesRepresentation'
tube8Display.PolarAxes = 'PolarAxesRepresentation'
tube8Display.SelectInputVectors = ['POINTS', 'Coordinates']
tube8Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tube8Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tube8Display.ScaleTransferFunction.Points = [-2.4164228439331055, 0.0, 0.5, 0.0, 5.030911922454834, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tube8Display.OpacityTransferFunction.Points = [-2.4164228439331055, 0.0, 0.5, 0.0, 5.030911922454834, 1.0, 0.5, 0.0]

# hide data in view
Hide(tTKScalarFieldNormalizer1, renderView9)

# hide data in view
Hide(tTKPersistenceDiagram1, renderView9)

# hide data in view
Hide(threshold9, renderView9)

# hide data in view
Hide(extractSurface2, renderView9)

# hide data in view
Hide(threshold10, renderView9)

# hide data in view
Hide(extractSurface3, renderView9)

# hide data in view
Hide(tube3, renderView9)

# hide data in view
Hide(extractSurface4, renderView9)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'y'
yPWF = GetOpacityTransferFunction('y')
yPWF.Points = [-4.233413219451904, 0.0, 0.5, 0.0, 4.233413219451904, 1.0, 0.5, 0.0]
yPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'x'
xPWF = GetOpacityTransferFunction('x')
xPWF.Points = [-5.03091287612915, 0.0, 0.5, 0.0, 5.03091287612915, 1.0, 0.5, 0.0]
xPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'CellDimension'
cellDimensionPWF = GetOpacityTransferFunction('CellDimension')
cellDimensionPWF.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]
cellDimensionPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'u'
uPWF = GetOpacityTransferFunction('u')
uPWF.Points = [-5.03091287612915, 0.0, 0.5, 0.0, 5.03091287612915, 1.0, 0.5, 0.0]
uPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'v'
vPWF = GetOpacityTransferFunction('v')
vPWF.Points = [-4.233413219451904, 0.0, 0.5, 0.0, 4.233413219451904, 1.0, 0.5, 0.0]
vPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'omega_bz'
omega_bzPWF = GetOpacityTransferFunction('omega_bz')
omega_bzPWF.Points = [0.49758370749999525, 0.0, 0.5, 0.0, 0.9639800145368502, 1.0, 0.5, 0.0]
omega_bzPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'CriticalType'
criticalTypePWF = GetOpacityTransferFunction('CriticalType')
criticalTypePWF.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]
criticalTypePWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# restore active source
SetActiveSource(tTKIcospheresFromPoints4)
# ----------------------------------------------------------------


if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')
