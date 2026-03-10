Full length article

# Simultaneous improvement of printability, mechanical isotropy, and high temperature strength in additively manufactured refractory multi-principal element alloy via ceramic powder additions and in-situ NbC nano-precipitation

<div style="text-align: center;"><img src="imgs/img_in_image_box_1001_296_1059_353.jpg" alt="Image" width="4%" /></div>


Ran Duan $ ^{a} $, Yakai Zhao $ ^{b,c} $ $ ^{d} $, Xiaodan Li $ ^{e} $, Jintao Xu $ ^{a} $, Meng Qin $ ^{a} $, Kai Feng $ ^{a,d,*} $ $ ^{e} $, Zhuguo Li $ ^{a,*} $, Beibei Xu $ ^{f,*} $, Upadrasta Ramamurty $ ^{g} $

 $ ^{a} $ Shanghai Key Laboratory of Materials Laser Processing and Modification, School of Materials Science and Engineering, Shanghai Jiao Tong University, Shanghai, 200240, PR China

Future Energy Acceleration & Translation (FEAT), Agency for Science, Technology and Research (A*STAR), Singapore, 138634, Singapore

 $ ^{c} $ Institute of Materials Research and Engineering (IMRE), Agency for Science, Technology and Research (A*STAR), Singapore, 138634, Singapore

 $ ^{d} $ School of Materials and Energy Engineering, Guizhou Institute of Technology, Guiyang, Guizhou, 550002, PR China

 $ ^{e} $ Shenyang Aircraft Corporation, Shenyang, 110000, PR China

 $ ^{1} $ State Key Laboratory of Materials for Integrated Circuits, Shanghai Institute of Microsystem and Information Technology, Shanghai, 200050, PR China

 $ ^{8} $ School of Mechanical and Aerospace Engineering, Nanyang Technological University, Singapore, 639798, Singapore

#### ARTICLE INFO

Keywords:

Refractory multi principal element alloys

Laser powder bed fusion

In-situ nano-precipitates

Printability

High-temperature strength

### A B S T R A C T

The inherent brittleness of the refractory multi-principal element alloys (RMPEAs) renders manufacturing of structural components with complex geometries using conventional means difficult. The additive manufacturing technique of laser powder bed fusion (LPBF) can potentially circumvent this problem. However, eliminating cracks, minimizing porosity, reducing the microstructural and (consequent) mechanical anisotropy, and retaining high-temperature (HT) strength—all simultaneously—remain the key challenges. Adding ceramic particles to the alloy can improve the printability and HT strength. However, the extreme melting points of RMPEAs can lead to their dissolution. Keeping this in view, 1.5 at. % WC powder—determined theoretically to be the optimum—was added to the  $ Nb_{15}Ta_{10}W_{75} $ powders prior to LPBF. Results show an expanded process window and improved printability, attributed to the enhanced laser absorptivity, without compromising powder flowability. Carbon released through the dissolution of WC combines with Nb to form NbC in-situ, which promotes in the columnar-to-equiaxed microstructural transition and hence reduced mechanical anisotropy. The NbC nanoprecipitates also enhance the high temperature strength (up to 1600 °C) by hindering the mobility of both screw and edge dislocations.

### 1. Introduction

The advent of multi-principal element alloys (MPEAs) has opened the arena of alloy design to a vast multicomponent space and enabled the identification of alloys with prominent properties for various applications[1–4]. Specifically, the refractory multi-principal element alloys (RMPEAs) exhibit excellent high-temperature (HT) strength and resistance to HT softening, making them potential candidates in a wide variety of high temperature applications [5–8]. Among RMPEAs reported thus far, NbMoTaW exhibits promising phase stability, resistance to softening at HT, and HT strength (~400 MPa at 1600 °C), far exceeding the service temperature of Ni-based superalloys [9]. While it is particularly suitable for HT pressure-bearing components, its intrinsic brittleness severely limits the application potential as producing components with complex shapes is difficult [10]. The additive manufacturing technique of laser powder bed fusion (LPBF) enables the direct fabrication of such components, overcoming the limitations (such as restricted mold shapes and poor processability) of arc melting [11–13]. However, two critical challenges remain for LPBF of NbMoTaW. First, the inherent brittleness of NbMoTaW could induce cracking.



under the high thermal gradients intrinsic to LPBF, making defect elimination particularly challenging  $ [14] $. Second, columnar grains preferentially form along the  $ [001] $ or  $ [101] $ crystallographic directions during LPBF, resulting in anisotropy that could adversely affect practical applications  $ [15,16] $. These challenges are addressed—primarily—by adding low-melting-point elements or ceramic particles to RMPEAs.

Incorporating low melting point (MP) elements (e.g., Ti, Zr, or Hf with the melting points of 1670, 1852, and 2227 °C, respectively) significantly enhances the constitutional undercooling (ΔT_CS). It, in turn, provides the driving force for heterogeneous nucleation and thus suppresses the columnar grain growth during LPBF [17,18]. However, alloying with elements with lower MP reduces the plastic flow softening temperature and promotes the transition of dislocation-mediated plastic deformation from that governed by cross-kinking to that of diffusion, thereby adversely affecting the HT strength [19–21]. It also could adversely affect the printability during LPBF. The significant thermodynamic differences (e.g., melting point, viscosity, and thermal expansion coefficient) between the high and low MP elements narrow the processing window and increase the risk of segregation-induced cracking owing to the increased volatility of low MP elements [21–23].

The addition of ceramic particles to alloys during LPBF can enhance heterogeneous nucleation, suppress columnar grains, and hinder dislocation mobility during HT deformation of the alloy  $ [24] $. The ceramic particles can also improve printability through the following possible mechanisms. They could (i) refine grains, which could help resist crack formation  $ [25] $, (ii) lower the melt viscosity, which would promote the molten metal flow in filling the pores  $ [26] $, (iii) enhance wettability that would facilitate stronger interlayer bonding  $ [27] $, and (iv) alleviate the tensile stresses generated during solidification by ceramic-induced compressive stress to suppress cracking  $ [28] $. The effectiveness of these mechanisms depends critically on the survival of ceramic particles within the melt pools of LPBF, as the high MP of RMPEA poses the risk of ceramic particle dissolution.

Keeping the above in mind, this work selectively incorporates nano-sized carbide particles into  $ Nb_{15}Ta_{10}W_{75} $ powders to improve printability by enhancing laser absorptivity. It also utilizes in-situ precipitation during LPBF to reduce the anisotropy and improve the room temperature (RT)/HT strengths. The roles of carbide particles and in-situ precipitates are further summarized in Supplementary-Note 1. This strategy effectively addresses the thermal stability limitations of ceramic particles in improving printability and HT strength in RMPEAs.  $ Nb_{15}Ta_{10}W_{75} $ alloy was chosen as the matrix, as it was optimized from the Nb-Mo-Ta-W alloy systems using the Toda-Caraballo model and demonstrated to exhibit an excellent HT strength of 640 MPa at 1600 °C [29]. The selection of ceramic particles involved the following three steps. (i) The type of non-metallic element within ceramic particles was determined by evaluating the solid solubility and melting point (obtained from the equilibrium phase diagram) of its in-situ formed compounds. (ii) The optimum ceramic content to be added was determined based on the critical re-precipitation amount (obtained from the non-equilibrium solidification path calculations) to ensure in-situ nano-precipitate formation during LPBF. (iii) The ceramic type was selected by evaluating mixed powder characteristics (including laser absorptivity and flowability), which can minimize the impact of the ceramic addition on the powder spreading characteristics and improve printing quality. The formation mechanisms of the NbC nano-precipitates, as well as their effects on microstructural evolution and RT/HT mechanical properties, were investigated in detail. Notably, the impact of NbC nano-precipitates on the screw/edge dislocation mobility at high temperatures is evaluated.

### 2. Materials and methodologies

#### 2.1. Material design and powder mixing

Since MPs of all the elements in the  $ Nb_{15}Ta_{10}W_{75} $ alloy are high, it is difficult to achieve a large degree of  $ \Delta T_{Cs} $. Adding suitable ceramic particles, which would act as the heterogeneous nucleation cites, is essential for achieving the columnar to equiaxed transition (CET) in it [13]. Since the high MP of  $ Nb_{15}Ta_{10}W_{75} $ can result in the dissolution of the added particles, the key strategy employed here is to add ceramic powders that can dissolve in the melt pools and, in the process, introduce a non-metallic element to the melt, which subsequently re-precipitate in-situ and regulates the grain morphology. The phase stability of the in-situ formed precipitates is an additional consideration that is crucial for maintaining grain morphology and strength of the alloy at HT. To this end, the solid solubility and melting points of various in-situ precipitations were assessed using an equilibrium phase diagram obtained from the Thermo-Calc software. An example of it is displayed in Fig. 1(a). It shows that with the incorporation of 0.25 at. % C into  $ Nb_{15}Ta_{10}W_{75} $, the matrix phase with the body centered cubic (BCC) crystal structure first solidifies, followed by the metal carbide (MC) phase at 2613 °C, with a maximum molar fraction of 1.1 %. Similar equilibrium phase diagrams were obtained when C, N, B, or O in different proportions were introduced into  $ Nb_{15}Ta_{10}W_{75} $, which all consist of BCC phase and in-situ precipitates (MC, MN, MB, or MO, respectively). The precipitation temperatures of MC, MN, MB, and MO are displayed in Fig. 1(b), and the maximum re-precipitation contents after adding different contents of C, N, B, or O into  $ Nb_{15}Ta_{10}W_{75} $ matrix are shown in Fig. 1(c). The MC phase has the highest precipitation temperature (the best phase stability) and re-precipitation content (the lowest solid solubility) compared to the MN, MB, and MO type precipitates. Therefore, it is inferred that adding C to  $ Nb_{15}Ta_{10}W_{75} $ aids in the in-situ formation precipitates and contributes to the phase stability.



To ensure the in-situ MC precipitation during LPBF, the non-equilibrium solidification paths of  $ (Nb_{15}Ta_{10}W_{75})_{100} - x_{Cx} $ ( $ \alpha = 0, 1.0, 1.5 $ at %) at a cooling rate of  $ 10^7 $ K/s were estimated using the Gulliver-Scheil model module (available in the Thermo-calc software) to determine the amount of C that needs to be added. Results are displayed in Figs.1 ( $ d_1 - d_2 $). The Gulliver-Scheil model is suitable for simulating the non-equilibrium solidification process that occurs under the rapid solidification conditions which prevail during the LPBF process [30]. This model assumes that complete diffusion occurs within the liquid phase, while no diffusion occurs in the solid phase [30]. Figures.1 ( $ d_1 - d_2 $) show that the solidification sequence remains liquid (L)→ BCC phase as long as the added C content is below 1.5 at %. It changes to L→ BCC→ BCC+MC when more than 1.5 at %. C. Therefore, incorporating more than 1.5 at. % C to  $ Nb_{15}Ta_{10}W_{75} $ is deemed beneficial for in-situ MC precipitation during LPBF.

While increasing the C content beyond 1.5 at. % can contribute positively to the precipitate formation during LPBF, it also could adversely affect the powder flowability, as it reduces the smoothness of the powder surfaces and thus enhances the rolling friction between the powder particles [31]. For determining the optimal type of carbide ceramic additions, the flowability and laser absorptivity of  $ Nb_{15}Ta_{10}W_{75} $ powders mixed with different ceramic powder contents were assessed. The detailed selection process is shown in Supplementary Note 2, and only the best results are presented below.

The required quantities of elemental powders (Nb, Ta, W, > 99.9 %

purity, Xiamen Tungsten Co.,Ltd., China) for forming  $ Nb_{15}Ta_{10}W_{75} $ were

accurately weighed using an electronic analytical balance. The pre-

mixed powders were put into a mixing tank and evacuated to a

vacuum of  $ 10^{-1} $ Pa before filling it with the argon gas. The pre-

mixed powder was then mixed at 120 r/min for 6 h in a three-dimensional

(3D) planetary mill. A laser diffraction analyzer (DC24000 UHR, CPS,

Inc.) was used to measure the equivalent diameter of the powders. The

 $ D_{10} $,  $ D_{50} $, and  $ D_{90} $ of the  $ Nb_{15}Ta_{10}W_{75} $ powders were 20, 37, and 57  $ \mu $m,

respectively. The powders display a spherical morphology, as shown in

Figs.2 (a1) and (b1). Then, WC powder was added to the  $ Nb_{15}Ta_{10}W_{75} $

powder such that the C content in the combined alloy corresponds to 1.5

% of the total at %; this alloy is referred to as ( $ Nb_{15}Ta_{10}W_{75} $) $ _{98.5}C_{1.5} $

hereafter. The WC powder size follows the Gaussian distribution and

<div style="text-align: center;"><img src="imgs/img_in_chart_box_91_113_441_596.jpg" alt="Image" width="29%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_444_115_753_367.jpg" alt="Image" width="25%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_789_116_1087_366.jpg" alt="Image" width="25%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_461_372_765_591.jpg" alt="Image" width="25%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_784_373_1093_592.jpg" alt="Image" width="25%" /></div>


<div style="text-align: center;">Fig. 1. (a) Equilibrium phase diagram and element compositions of  $ Nb_{15}Ta_{10}W_{75} $ doped with non-metallic elements. (b) Precipitation temperatures of MC, MN, MB, MO. (c) Comparison of the molar fractions of different in-situ precipitated phases for different non-metallic element additions. Selection of non-metallic element content based on the solidification path for  $ (\mathrm{Nb}_{15}\mathrm{Ta}_{10}\mathrm{W}_{75})_{100-\mathrm{x}}\mathrm{C}_{\mathrm{x}}:(\mathrm{d}_{1}) $ x = 0 at. %; ( $ d_{2} $); x = 1.5 at. %.</div>


was found to be uniformly distributed on the surfaces of the  $ Nb_{15}Ta_{10}W_{75} $ powders after being mixed in a planetary mill for 5 h, as shown in Figs. 2(a2) and (b2). The flowability of powders, which is crucial for printing quality, was evaluated by using the Hall flowmeter [32]. Both the Hall flow rate (HRF) and the angle of repose (AOR) did not show significant changes after the incorporation of WC powders, as shown in Figs.2 (c1-c2), indicating that it will not affect the powder flow and spread.

Apart from powder flowability, laser absorptivity also significantly influences print quality. The addition of smaller WC particles to the  $ Nb_{15}Ta_{10}W_{75} $ powder increases its convex and specific surface areas and thus could enhance its laser absorptivity and reduce the energy required for melting powders [32]. To ascertain this, the laser absorptivity was measured using the diffuse reflectance spectroscopy (DRS, UV–vis–NIR Lambda 950 Spectrophotometer, PerkinElmer, Inc.). The laser absorptivity of the  $ Nb_{15}Ta_{10}W_{75}98.5C_{1.5} $ powders is 88 % higher (at a wavelength of 1070 nm used for the LPBF process) than that of the  $ Nb_{15}Ta_{10}W_{75} $ powders, as shown in Figs.2 (d1–d2). Thus, incorporation of 1.5 at. % WC powders into  $ Nb_{15}Ta_{10}W_{75} $ aids in the in-situ precipitation as well as fabrication using LPBF.



#### 2.2. Material preparation

The LPBF processes were carried in an SLM 280 metal printer (Zhong Rui Technique, China), which was equipped with a maximum laser power of 500 W (YAG fiber laser; beam spot diameter 90  $ \mu $m; wavelength 1070 nm). The process chamber was filled with high-purity argon (99.999 vol %; oxygen content below 100 ppm) and shielded the sam-

<div style="text-align: center;"><img src="imgs/img_in_image_box_186_1021_426_1219.jpg" alt="Image" width="20%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_426_1025_730_1227.jpg" alt="Image" width="25%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_736_1024_1002_1223.jpg" alt="Image" width="22%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_187_1230_421_1429.jpg" alt="Image" width="19%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_423_1229_728_1433.jpg" alt="Image" width="25%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_733_1230_1002_1431.jpg" alt="Image" width="22%" /></div>


<div style="text-align: center;">Fig. 2. Surface morphology of (a₁) Matrix powders and (a₂) Mixed powders; Particle size distribution of (b₁) Matrix powders and (b₂) WC powder additions; HRF and AOE of (c₁) Matrix powders and (c₂) Mixed powders; Laser absorptivity of (d₁) Matrix powders and (d₂) Mixed powders.</div>


ples from oxidation. A rotation angle of 67 ° between successive layers was applied to reduce stress and anisotropy. A polished pure tungsten plate was used as the substrate to improve the bonding with the material. The melting points of Nb, Mo, Ta, and W all exceeded 2400 °C [8], requiring high energy input to melt the powders during LPBF completely. To analyze the influence of WC powder addition on the optimum printing process parameter window of Nb₁₅Ta₁₀W₇₅, a series of samples were printed using different volumetric energy densities (VED) [33]:

 $$ VED=\frac{P}{vht}. $$ 

In Eq. (1), P is laser power, v is the scanning speed, h is the hatch spacing, and t is the layer thickness. A total of 480 process parameter combinations, with the VED and P ranges of 50 to 850 J/mm³ and 150 to 400 W, respectively, for each composition were explored. In all cases, t was fixed at 40 μm, while h was either 30 or 40 μm, v was adjusted accordingly based on the above parameters. Based on these trails, the following optimum process parameter combination for Nb₁₅Ta₁₀W₇₅ was identified: P = 300 W, v = 400 mm/s, t = 40 μm, and h = 30 μm. With the addition of 1.5 at. % WC powder, a v of 690 mm/s (while the other three process parameters remained the same) gave the best results.

A gas expansion density tester (HX-TD, Hiseel, China) was used to measure the relative density of the printed samples. This device measured the variation in helium gas volume within the test chamber before and after placing the sample, providing an efficient, accurate, and non-destructive method to measure the true volume and density of the printed samples. To ensure measurement accuracy, the printed samples were successively polished using the 500 #, 1000 #, 1500 #, 2000 # and 3000 # grit sandpapers to minimize the influence of irregular surface contours. For each printing parameter combination, nine samples were printed, and their density was measured, with each sample tested 3 times to ensure the reliability of the results. Cubic samples of  $ 8 \times 8 \times 10 $ mm $ ^3 $ were printed and used for density measurement, microstructural characterization, and compression experiments.

### 2.3. Microstructural and mechanical characterization

The crystal structure of the phase(s) in the microstructure was analyzed by using the X-ray diffraction (XRD; D8 Advance Da Vinci, Bruker Corp., USA) equipped with Cu-Kα radiation (λ = 1.5418 Å) operating at 40 kV, 40 mA, and performed over a scan range of 20 ° and 100 ° with a scan rate of 1.5 °/min. The defect characteristics of the printed samples were characterized using an optical microscope (OM; Axio Imager A2m, Zeiss, Germany). Microstructural characteristics and powder morphology were observed with the aid of a scanning electron microscope (SEM; FEI Co., Hillsboro, OR, USA). It was equipped with the energy dispersive spectroscopy (EDS) and electron backscatter diffraction (EBSD) detectors, which were used to analyze the microscopic segregation and the grain orientation, respectively. The EBSD experiments were performed at an accelerating voltage of 20 kV with a scan step size of 0.1 μm. The finer microstructures and precipitates were observed by using transmission electron microscopy (TEM; JEM-F200X, JEOL Ltd., Tokyo, Japan) working at a voltage of 200 kV. For TEM, foils were prepared by a focused ion beam (FIB; Carl Zeiss AG) equipped with an electron beam at 100 kV. The elemental distribution within the precipitates was characterized using the 3D-atom probe tomography (3D-APT; LEAP 5000X), operating at a pulse repetition rate of 200 kHz and a UV laser energy of 60 pJ. The sharp tipped samples for 3D-APT were fabricated by annular milling within the grains using FIB.

Uniaxial compression experiments were performed in a universal testing machine (Sans Testing Machine Co., Ltd., Shenzhen, China) equipped with a video extensometer (LVE-MICRO30) at a nominal constant loading rate of 0.008 mm/s. The size of compression specimens was Φ2 mm × 4 mm. At least three samples were tested for each case. The HT compression properties were measured by using a Gleeble-3500 testing machine, with a heating rate of 10 °C/min and a constant displacement rate (εL) of 0.0025 mm/s. The size of HT compression specimens was Φ4 mm × 8 mm.



### 3. Results

#### 3.1. Sample preparation

Results of the defect morphologies of the printed samples, characterized using OM, and their relative densities, measured using a gas expansion density tester, are shown in Fig. 3(a). For VED below 310 J·mm⁻³, lack of fusion (LOF) pores were observed in both Nb₁₅Ta₁₀W₇₅ and (Nb₁₅Ta₁₀W₇₅)₉₈.C₁.₅. They are likely due to inadequate heat input for fully melting refractory metal powders [34,35]. When VED exceeded 620 J·mm⁻³, cracks were observed in both RMPEAs. Cracking is thought to be driven by the accumulation of thermal stresses, caused by the excessive energy input [23]. The optimal VED ranges for Nb₁₅Ta₁₀W₇₅ and (Nb₁₅Ta₁₀W₇₅)₉₈.C₁.₅ were found to be 520–620 J·mm⁻³ and 360–520 J·mm⁻³, which resulted in the densities of 99.2 ± 0.15 % and 99.5 ± 0.1 %, respectively, with pores being the only type of defects present in the blocks fabricated using these parameters. The incorporation of WC powders not only led to a higher density—that too at a lower VED, but also a wider process window (extended by 50 J·mm⁻³), compared to Nb₁₅Ta₁₀W₇₅, possibly due to the enhanced laser absorptivity (Fig. 2(d₂)). Cuboidal samples (8 × 8 × 10 mm³) of both the alloys were manufactured with the optimal process (mentioned in Section 2.2) and are used for microstructure characterization and compression experiments, as shown in Fig. 3(b).

### 3.2. Microstructural characterization

The XRD patterns obtained on Nb₁₅Ta₁₀W₇₅ and (Nb₁₅Ta₁₀W₇₅)₉₈.₅C₁.₅ are shown in Fig. 4. The pattern obtained on Nb₁₅Ta₁₀W₇₅ shows a single phase with the BCC crystal structure. With the incorporation of WC powder, additional peaks corresponding to the NbC precipitates with B₂ crystal structure are observed. The dislocation density (ρ) within the built samples was estimated using the XRD data and the following equations [36,37]:

 $$ \rho=\frac{2\sqrt{3}\vartheta}{\psi b} $$ 

 $$ \vartheta=\frac{\beta}{4tan\theta} $$ 

 $$ \psi=\frac{K\lambda}{\beta cos\theta} $$ 

where $\vartheta$ is the micro-strain (which is related to the full width at half maximum (FWHM) of the XRD peak, $\beta$ [38]), $\psi$ is the coherent domain size (that depends on the X-ray wavelength, $\lambda = 0.15405$ nm [38,39]), $b$ is the Burgers vector, $\theta$ is the Bragg angle, and $K$ is a dimensionless factor (= 0.89 [39]). Details of the calculations used for estimating $\rho$ based on the XRD data are provided in Supplementary-Note 3. The estimated $\rho$ values in Nb$_{15}$Ta$_{10}$W$_{75}$ and (Nb$_{15}$Ta$_{10}$W$_{75}$)$_{98.5}$C$_{1.5}$ are about $3.36 \pm 0.2 \times 10^{14}$ and $3.96 \pm 0.3 \times 10^{14}$ $m^{-2}$, respectively.

Figs. 5 (a1–a4) display the SEM images of the X-Y and X-Z planes of  $ Nb_{15}Ta_{10}W_{75} $ and  $ Nb_{15}Ta_{10}W_{75}g_{8.5}C_{1.5} $. They show few pores and no cracks, confirming the high relative densities and good quality prints. The inverse pole figure (IPF) maps (overlapped with the high-angle grain boundaries (HAGBs) for showing grain morphologies) are displayed in Figs. 5 (b1–b4). Generally, the misorientation angles between neighboring grains exceed 15° for HAGBs, while the low-angle grain boundaries (LAGBs) are those grain boundaries (GBs) with misorientation angles between 2° and 15° [40]. In the X-Y plane, both the alloys do not exhibit significant columnar grain morphology. In the X-Z plane,  $ Nb_{15}Ta_{10}W_{75} $ exhibits a columnar grain morphology, with the long axis

<div style="text-align: center;"><img src="imgs/img_in_chart_box_190_110_524_373.jpg" alt="Image" width="28%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_522_113_1003_370.jpg" alt="Image" width="40%" /></div>


<div style="text-align: center;">Fig. 3. (a) OM images combined with gas expansion densities at different VEDs illustrate the variations in the defect characteristics, relative density, and process window after the WC powder addition; (b) Display of  $ Nb_{15}Ta_{10}W_{75} $ and  $ Nb_{15}Ta_{10}W_{75} $_{98.5}C_{1.5} samples used for microstructure characterization and compression experiments.</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_82_486_566_741.jpg" alt="Image" width="40%" /></div>


<div style="text-align: center;">Fig. 4. X-ray diffraction patterns obtained on the  $ Nb_{15}Ta_{10}W_{75} $ and  $ (\mathrm{Nb}_{15}\mathrm{Ta}_{10}\mathrm{W}_{75})_{98.5}\mathrm{C}_{1.5} $.</div>


of the grains oriented along the Z-axis direction. This is due to the significant temperature gradient along the Z-axis, which leads to the formation of columnar grains aligned with it [39].

To further identify the grain morphology, the grain shape aspect ratio (GSAR) is analyzed, as shown in Figs.5 (c1–c4). The GSAR is defined as the ratio of the short to long axis of the grains, with distinct colors used to differentiate grain morphologies. Both  $ Nb_{15}Ta_{10}W_{75} $ and  $ Nb_{15}Ta_{10}W_{75}98.5C_{1.5} $ exhibit cellular grain morphology on the X-Y plane. The GSAR values are closely concentrated in the range of 0.3–0.6, comprising 66.3 % for  $ Nb_{15}Ta_{10}W_{75} $ and 63.5 % for  $ Nb_{15}Ta_{10}W_{75}98.5C_{1.5} $, as shown in Figs.5 (c1) and (c3). The GSAR of  $ Nb_{15}Ta_{10}W_{75}98.5C_{1.5} $ on the X-Z plane increases significantly compared to that of  $ Nb_{15}Ta_{10}W_{75} $, particularly in the range of 0.3–0.6, rising from 35.5 % to 71.0 %, as shown in Figs.5 (c2) and (c4). This indicates a significant increase in short axis grains, and the addition of WC powders effectively inhibits the growth of columnar grains. Besides, GSAR maps over a larger area (500 µm × 600 µm) on the X-Z plane were obtained to further distinguish grain morphology (Figs.5 (d1–d2)). The results indicate that  $ Nb_{15}Ta_{10}W_{75}98.5C_{1.5} $ has a higher GSAR value, with a high proportion of 69.9 % at 0.3–0.6 and 8.7 % at 0.6–1.0, indicating the WC powder addition suppresses the columnar grain growth and results in an equiaxed microstructure.

Except for grain morphology, the pole figures (PFs) also confirm that the addition of WC powders suppresses the columnar grain growth, as shown in Figs.5 (e1–e4). In the X-Y plane, random texture is noted for both the alloys (Fig. 5(e1) and (e3)). The maximum uniform distribution (MUD) values are 2.93 and 2.83 for  $ Nb_{15}Ta_{10}W_{75} $ and  $ (Nb_{15}Ta_{10}W_{75})_{98.5}C_{1.5} $, respectively. In the X-Z plane of  $ Nb_{15}Ta_{10}W_{75} $, strong  $ \{100\} $ texture can be observed (Fig. 5(e2)), which is the preferred grain growth direction during LPBF [10,11]. The corresponding MUD value is 3.29. With the WC powder addition, significant reduction in the intensity of  $ \{100\} $ texture is noted, making the texture random (Fig. 5(e4)). Correspondingly, the MUD value decreased to 3.02.



Bright-field (BF) TEM images obtained from the Nb₁₅Ta₁₀W₇₅ and (Nb₁₅Ta₁₀W₇₅)₉₈.₅C₁.₅ samples are shown in Figs.6 (a₁) and (a₂), respectively. (Nb₁₅Ta₁₀W₇₅)₉₈.₅C₁.₅ contains a large number of dispersed precipitates, which were uniformly distributed both within the grains and at the GBs. Selected area electron diffraction (SAED) patterns of Nb₁₅Ta₁₀W₇₅, obtained using the [01–1]BCC zone axis, and (Nb₁₅Ta₁₀W₇₅)₉₈.₅C₁.₅ along the [1–31]BCC zone axis, are shown in Figs.6 (b₁) and (b₂), respectively. Nb₁₅Ta₁₀W₇₅ exhibits only a BCC structure without any second phase. In contrast, (Nb₁₅Ta₁₀W₇₅)₉₈.₅C₁.₅ displays an additional set of diffraction spots, which correspond to the B₂ crystal structure, indicating the in-situ formation of MC precipitates. The phase structures observed from the SAED patterns are consistent with the XRD results shown in Fig. 4. An EDS line scan, performed on the nanoprecipitates inside the grains (red dashed box), is shown in Fig. 6(c). The C and Nb contents are the highest in the center of the nano-scale precipitate, while other elements are significantly lower. Especially, the W content is significantly lower in the precipitate than in the matrix, whereas Ta content is nearly constant. The elemental distribution confirms that the observed particles are indeed NbC nano-precipitates, with the length and width of about 67 ± 5 and 45 ± 4 nm respectively.

Fig.6(d) displays the TEM dark-field (DF) micrographs of the NbC precipitates within (Nb₁₅Ta₁₀W₇₅)₉₈.₅C₁.₅, which is obtained along the [222]ₙbC zone axis (Fig. 6(e)). The results show that a considerable number of precipitates are uniformly distributed in the alloy. Based on the DF-TEM images, the average diameter (r) of these precipitates (measured using the Image-Pro-Plus software) is determined to be 37.2

 $ \pm 4.3 \, nm $ (Fig. 6(f)). Their number density (N) was estimated by using the following equations [40]:

 $$ N=\frac{f}{4/3\pi r^{3}} $$ 

 $$ f=\frac{\sum_{i}\pi r_{i}^{2}T_{avg}}{2x_{p}y_{p}t_{d}} $$ 

 $$ T_{avg}=1.15R(1)+2.07R(2)+2.99R(3)+3.91R(4) $$ 

where $f$ is the volume fraction. $T_{avg}$ is the average thickness of NbC, taken across four different locations ($R(i)$) of the TEM sample [40], $x_p$ and $y_p$ are the dimensions of the TEM image, and $t_d$ is the thickness of the TEM sample. The obtained $N$ value of the NbC precipitate, $9.7 \pm 3.8 \times 10^{22} \, m^{-3}$, suggests that a large amount of NbC precipitates were uniformly dispersed in ($Nb_{15}Ta_{10}W_{75}$)98.5C1.5 RMPEAs.

For  $ Nb_{15}Ta_{10}W_{75} $, the typical atomic structure of the matrix is observed from the intragranular region using HRTEM (Fig. 7(a)). The HRTEM image of this region is enlarged, and the corresponding Fast Fourier transform (FFT) images are shown in Figs.7 ( $ b_{1} $) and ( $ b_{2} $),

<div style="text-align: center;"><img src="imgs/img_in_image_box_183_111_1007_1169.jpg" alt="Image" width="69%" /></div>


<div style="text-align: center;">Fig. 5. Effect of adding WC powders on defects and grain morphologies. (a₁-a₄) SEM images showing high density with fewer defects. (b₁-b₄) IPF maps overlapping with HAGBs showing the grain morphology. (c₁-c₄) GSAR maps and (d₁-d₂) Extended-range measurement GSAR maps used to distinguish grain morphology. (e₁-e₄) Pole figures showing the variations in the texture.</div>


respectively. The selected area exhibits a BCC structure without additional diffraction spots, consistent with the results of SAED (Fig. 6(b)). The interplanar spacing along  $ [011]_{BCC} $ was measured as 0.22 nm, which corresponds to a lattice parameter of 3.22 Å. Fig. 7(c) shows the crystal structures of the matrix, NbC/matrix interface, and NbC in  $ (Nb_{15}Ta_{10}W_{75})_{98.5}C_{1.5} $. High-magnification HRTEM images and FFT patterns of the nano-precipitates are shown in Figs. 7 (d1-d2), (e1-e2), and (f1-f2), respectively. Only one set of diffraction spots is present in the matrix (Fig. 7(d2)) and NbC (Fig. 7(f2)). In contrast, two sets of diffraction spots are observed at the NbC/matrix interface (Fig. 7(e2)), confirming the phase relationship of  $ [011]_{BCC}/[0-1-1]_{NbC} $. The measured interplanar spacings of  $ [011]_{BCC} $ and  $ [011]_{NbC} $ are 0.224 nm (Fig. 7(d1)) and 0.231 nm (Fig. 7(f1)), respectively, with corresponding lattice parameters of 3.26 and 3.36 Å. The lattice mismatch ( $ \delta $) between the BCC matrix and NbC nano-precipitates was estimated using the following equation [42]:



 $$ \delta=\frac{\alpha_{NbC}-\alpha_{BCC}}{\alpha_{NbC}} $$ 

where  $ \alpha_{NbC} $ and  $ \alpha_{BCC} $ are the lattice parameters of the carbide and BCC

<div style="text-align: center;"><img src="imgs/img_in_image_box_181_112_1005_803.jpg" alt="Image" width="69%" /></div>


<div style="text-align: center;">Fig. 6. (a1-a2) Representative TEM bright-field images obtained from the Nb15Ta10W75 and (Nb15Ta10W75)98.5C1.5 samples. Insets (b1–b2) show the corresponding SAED patterns. (c) EDS line scans showing the compositional distribution inside the nano-precipitates. (d) A TEM dark-field image of (Nb15Ta10W75)98.5C1.5 containing NbC precipitates and (e) the corresponding SAED pattern. (f) Normal distribution pattern of NbC precipitates.</div>


phases. The lattice mismatch between the BCC matrix and NbC is estimated to be 2.9 % (<5 % [28,41,42]), indicating that the interface between NbC and the matrix is coherent (Fig. 7(e1)).

### 3.3. Mechanical properties

Representative compressive engineering stress-strain responses and fracture morphologies are shown in Fig. 8. The mechanical properties at different temperatures are listed in Table 1. Nb15Ta10W75 displays significant mechanical anisotropy, as seen from Figs. 8(a1) and (a2). The compressive yield strength (σ0,2), ultimate compressive strength (σm), and fracture strain (ε) at RT and parallel to BD are 759 ± 17 MPa, 939 ± 16 MPa, and 2.6 ± 0.2 %, respectively. Perpendicular to BD, they are 1409 ± 22 MPa, 1520 ± 13 MPa, and 5.3 ± 0.3 %, respectively. The σ0,2 and ε values in the direction perpendicular to BD are nearly-double of those along BD, illustrating significant anisotropy. In contrast, incorporating WC powder into Nb15Ta10W75 effectively eliminates the mechanical anisotropy due to CET (Fig. 5). In addition, σ0,2, σm, and ε along BD increased significantly to 1591 ± 25 MPa, 1667 ± 13 MPa, and 7.4 ± 0.1 %, respectively. Perpendicular to BD, they increased to 1615 ± 28 MPa, 1692 ± 21 MPa, and 8.3 ± 0.4 %, respectively. Note that σ0,2 and ε of (Nb15Ta10W75)98.5C1.5 in the two orientations are nearly the same.

The fractographs obtained from the specimens tested in different orientations are shown in Figs.8 (b₁-b₄). For Nb₁₅Ta₁₀W₇₅, fractographs of specimens tested along BD show cleavage fracture characteristics, with relatively smooth surfaces and river patterns (Fig. 8(b₁)). When compressed in the direction perpendicular to BD, the fractured surface exhibits a mixture of cleavage and quasi-cleavage fracture characteristics (Fig. 8(b₃)). After adding WC powder, the fracture mechanism across both compression directions transitions to quasi-cleavage fracture, exhibiting a greater number of torn edges (Figs.8 (b₂) and (b₄)).



The stress–strain responses of  $ Nb_{15}Ta_{10}W_{75} $ and  $ (\mathrm{Nb}_{15}\mathrm{Ta}_{10}\mathrm{W}_{75})_{98.5}\mathrm{C}_{1.5} $, with the compression direction perpendicular to BD, at HT are shown in Figs.8 ( $ c_{1-c4} $). At 1000, 1200, and 1400 °C, the stress-strain curves for  $ Nb_{15}Ta_{10}W_{75} $ and  $ (\mathrm{Nb}_{15}\mathrm{Ta}_{10}\mathrm{W}_{75})_{98.5}\mathrm{C}_{1.5} $ exhibit elastic deformation before fracture, with some limited plasticity only observed at 1600 °C. This is probably due to the transition from cross-kinking to a diffusion-controlled dislocation slip mechanism at higher temperatures, facilitating dislocation slip and hence plastic deformation [43]. More importantly,  $ \sigma_{0.2} $ of  $ (\mathrm{Nb}_{15}\mathrm{Ta}_{10}\mathrm{W}_{75})_{98.5}\mathrm{C}_{1.5} $ over the temperature range of 1000 and 1600 °C exceed those of  $ Nb_{15}\mathrm{Ta}_{10}\mathrm{W}_{75} $ by about 100 MPa. The mechanical test results indicate that the incorporation of WC powder into  $ Nb_{15}\mathrm{Ta}_{10}\mathrm{W}_{75} $ can eliminate anisotropy, improve RT plasticity, and enhance strength at both RT and HT.

### 4. Discussion

### 4.1. Formation mechanisms of the NbC precipitates

From Fig. 6, it is obvious that the WC particles added to the RMPEA powder completely dissolves during the LPBF process, and then lead to the formation of the NbC nano-precipitates within the matrix. These precipitates suppress the columnar grain growth, and, in turn, reduce the mechanical anisotropy (Figs. 5 and 8). It is well known that in-situ

<div style="text-align: center;"><img src="imgs/img_in_image_box_182_115_1002_752.jpg" alt="Image" width="68%" /></div>


<div style="text-align: center;">Fig. 7. (a) HRTEM image, (b1) an enlarged HRTEM image, and (b2) the corresponding FFT pattern obtained on  $ Nb_{15}Ta_{10}W_{75} $. (c) HRTEM image of the interface between BCC matrix and NbC precipitate in  $ (Nb_{15}Ta_{10}W_{75})_{98.5}C_{1.5} $. Magnified HRTEM images and corresponding FFT patterns used to analyze the crystal structure at different locations of  $ (d_{1}-d_{2}) $ the BCC matrix,  $ (e_{1}-e_{2}) $ the NbC/matrix interface, and  $ (f_{1}-f_{2}) $ the NbC precipitates.</div>


precipitation during LPBF facilitates CET [44]. Therefore, the mechanisms responsible for the NbC formation in (Nb $ _{15} $Ta $ _{10} $W $ _{75} $) $ _{98.5} $C $ _{1.5} $ need elucidation, which is attempted in the following through a comparative analysis of the physical characteristics and precipitation kinetics.

Generally, a lower mixing enthalpy ( $ \Delta H_{mix} $) indicates a stronger affinity between the elements, which favors the formation of stable compounds during LPBF [45]. The values of  $ \Delta H_{mix} $ of Nb, Ta, and W with C are shown in Fig. 9(a). Amongst them, Nb-C exhibits the lowest  $ \Delta H_{mix} $ compared to Ta-C and W-C, suggesting a strong preference for forming NbC. This observation rationalizes their in-situ formation during LPBF of (Nb $ _{15} $Ta $ _{10} $W $ _{75} $) $ _{98.5} $C $ _{1.5} $. Notably, the comparison of  $ \Delta H_{mix} $ values among metallic compounds provides a meaningful starting point for the kinetic calculations (including precipitate nucleation and growth), ensuring that the predicted phase was the most thermodynamically favorable one, while ruling out metastable phases (for example,  $ \Delta H_{mix} $ for W-C is -60 kJ/mol). The nucleation of precipitates is predominantly influenced by the thermodynamic driving force ( $ \Delta G^{*} $), which influences the nucleation rate ( $ N_v $) [46,47]. Using the Thermo-Calc software, values for  $ \Delta G^{*} $ and  $ N_v $ of the BCC and NbC phases that are included in the non-equilibrium solidification curve 2 of Fig. 1(d2) are obtained. Results are shown in Figs. 9 (b-c). The maximum  $ \Delta G^{*} $ value of NbC (6177 J) is nearly-seven times that of the BCC phase (851 J), resulting in  $ N_v $ for NbC being about  $ 10^7 $ times higher than that for BCC phase. On this basis, it is reasonable to assume that NbC nucleates rapidly (even at high cooling rates ( $ 10^7 $ K/s) that prevail during LPBF).

The diffusion coefficient ( $ \zeta $) also plays a critical role in the nucleation and growth of NbC [48]. The  $ \zeta $ values of Nb, Ta, W, and C are estimated using the following equation [49]:

 $$ \varsigma=\varsigma_{0}exp\left(\frac{-Q_{D}}{RT}\right) $$ 

where  $ \varsigma_0 $ is the intrinsic diffusion coefficient (m²/s) and  $ Q_D $ is the activation energy for diffusion (kJ/mol). These parameters are obtained from literature through experiments or simulations of refractory metals composed of Nb, Ta, and W [49], and listed in Table 2. The temperature-dependence of  $ \varsigma $ for Nb, Ta, W, and C is shown in Fig. 9(d). The results indicate that C has significantly higher  $ \varsigma $ than the metallic elements across different temperatures, which would also facilitate the in-situ formation of carbides including NbC. Overall, the small  $ \Delta H_{mix} $ as well as large  $ \Delta G^* $,  $ N_\nu $,  $ \varsigma $ of NbC, are possibly the reasons that ensure the nucleation and growth of NbC during LPBF.

Variations in the phase volume fractions and element contents under the conditions of non-equilibrium solidification ( $ 10^7 $ K/s) are analyzed to further explore the origin of in-situ formed NbC. The non-equilibrium cooling path containing NbC is shown in Fig. 10(a), which is derived from stage 2 of the non-equilibrium cooling curve depicted in Fig. 1(d). The variations in the volume fractions of the liquid, BCC and NbC phases with the temperature are shown in Fig. 10(b). As the temperature decreases from 2755 to 2680 °C at a cooling rate of  $ 10^7 $ K/s, the liquid phase simultaneously transforms into BCC and NbC phases. Within this temperature range, the formation temperature of NbC (2740 °C) slightly lags behind that of the BCC phase (2753 °C), with higher  $ 4G^* $,  $ N_\nu $, and  $ \xi $ values promoting the transformation. The phase transformation pathways are governed by elemental redistribution. Therefore, the ThermoCalc software was employed to calculate the compositional variations under non-equilibrium cooling conditions ( $ 10^7 $ K/s). Results, shown in Figs. 10 (c1-c4), indicate that, during the formation of NbC,

<div style="text-align: center;"><img src="imgs/img_in_chart_box_184_112_600_355.jpg" alt="Image" width="34%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_605_112_1006_355.jpg" alt="Image" width="33%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_184_360_404_587.jpg" alt="Image" width="18%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_609_361_805_582.jpg" alt="Image" width="16%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_811_360_1006_584.jpg" alt="Image" width="16%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_182_593_405_851.jpg" alt="Image" width="18%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_412_595_605_852.jpg" alt="Image" width="16%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_612_595_809_872.jpg" alt="Image" width="16%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_814_598_1006_872.jpg" alt="Image" width="16%" /></div>


<div style="text-align: center;">Fig. 8. Compression engineering stress-strain curves at RT of the (a₁) vertical sample and (a₂) horizontal sample; RT compression fracture morphology of the (b₁-b₂) vertical samples and (b₃-b₄) horizontal samples; HT stress-strain curves at (c₁) 1000, (c₂) 1200, (c₃) 1400, and (c₄) 1600 °C.</div>


<div style="text-align: center;">Mechanical properties of Nb $ _{15} $Ta $ _{10} $W $ _{75} $ and (Nb $ _{15} $Ta $ _{10} $W $ _{75} $) $ _98.5 $C $ _{1.5} $ along different compression directions.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td rowspan="2"></td><td rowspan="2"></td><td colspan="3">Nb_{15}Ta_{10}W_{75}</td><td colspan="3">(Nb_{15}Ta_{10}W_{75})_{98.5}C_{1.5}</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \sigma_{0.2} $ (MPa)</td><td style='text-align: center; word-wrap: break-word;'>$ \sigma_{m} $ (MPa)</td><td style='text-align: center; word-wrap: break-word;'>$ \varepsilon $ (%)</td><td style='text-align: center; word-wrap: break-word;'>$ \sigma_{0.2} $ (MPa)</td><td style='text-align: center; word-wrap: break-word;'>$ \sigma_{m} $ (MPa)</td><td style='text-align: center; word-wrap: break-word;'>$ \varepsilon $ (%)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Parallel-BD</td><td style='text-align: center; word-wrap: break-word;'>25 °C</td><td style='text-align: center; word-wrap: break-word;'>759  $ \pm $ 17</td><td style='text-align: center; word-wrap: break-word;'>939  $ \pm $ 16</td><td style='text-align: center; word-wrap: break-word;'>2.6  $ \pm $ 0.2</td><td style='text-align: center; word-wrap: break-word;'>1591  $ \pm $ 25</td><td style='text-align: center; word-wrap: break-word;'>1667  $ \pm $ 13</td><td style='text-align: center; word-wrap: break-word;'>7.4  $ \pm $ 0.1</td></tr><tr><td rowspan="5">Perpendicular-BD</td><td style='text-align: center; word-wrap: break-word;'>25 °C</td><td style='text-align: center; word-wrap: break-word;'>1409  $ \pm $ 22</td><td style='text-align: center; word-wrap: break-word;'>1520  $ \pm $ 13</td><td style='text-align: center; word-wrap: break-word;'>5.3  $ \pm $ 0.3</td><td style='text-align: center; word-wrap: break-word;'>1615  $ \pm $ 28</td><td style='text-align: center; word-wrap: break-word;'>1692  $ \pm $ 21</td><td style='text-align: center; word-wrap: break-word;'>8.3  $ \pm $ 0.4</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1000 °C</td><td style='text-align: center; word-wrap: break-word;'>1009  $ \pm $ 10</td><td style='text-align: center; word-wrap: break-word;'>1451  $ \pm $ 13</td><td style='text-align: center; word-wrap: break-word;'>15.9  $ \pm $ 0.5</td><td style='text-align: center; word-wrap: break-word;'>1105  $ \pm $ 31</td><td style='text-align: center; word-wrap: break-word;'>1602  $ \pm $ 15</td><td style='text-align: center; word-wrap: break-word;'>16.4  $ \pm $ 0.1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1200 °C</td><td style='text-align: center; word-wrap: break-word;'>942  $ \pm $ 27</td><td style='text-align: center; word-wrap: break-word;'>1372  $ \pm $ 21</td><td style='text-align: center; word-wrap: break-word;'>17.2  $ \pm $ 0.4</td><td style='text-align: center; word-wrap: break-word;'>1042  $ \pm $ 29</td><td style='text-align: center; word-wrap: break-word;'>1513  $ \pm $ 22</td><td style='text-align: center; word-wrap: break-word;'>15.0  $ \pm $ 0.2</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1400 °C</td><td style='text-align: center; word-wrap: break-word;'>841  $ \pm $ 25</td><td style='text-align: center; word-wrap: break-word;'>1242  $ \pm $ 24</td><td style='text-align: center; word-wrap: break-word;'>14.4  $ \pm $ 0.1</td><td style='text-align: center; word-wrap: break-word;'>952  $ \pm $ 20</td><td style='text-align: center; word-wrap: break-word;'>1397  $ \pm $ 24</td><td style='text-align: center; word-wrap: break-word;'>14.8  $ \pm $ 0.8</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1600 °C</td><td style='text-align: center; word-wrap: break-word;'>640  $ \pm $ 18</td><td style='text-align: center; word-wrap: break-word;'>744  $ \pm $ 9</td><td style='text-align: center; word-wrap: break-word;'>14.6  $ \pm $ 0.5</td><td style='text-align: center; word-wrap: break-word;'>750  $ \pm $ 16</td><td style='text-align: center; word-wrap: break-word;'>957  $ \pm $ 12</td><td style='text-align: center; word-wrap: break-word;'>15.3  $ \pm $ 0.7</td></tr></table>

and Nb rapidly diffuse to it in the liquid phase, reaching 18.5 and 68.5 at. %, respectively. On the other hand, W segregates to the BCC phase, reaching 78.4 %. Ta is relatively uniformly distributed in both the phases, with concentrations of 15.9 and 8.5 at. %, respectively. The combination of (i) rapid cooling process of LPBF [13], (ii) the low diffusion rate of refractory metals (Fig. 9(d)), and (iii) the minimal variation in elemental composition during non-equilibrium solidification (Fig. 10 (c1-c4)), result in the preservation of precipitate compositions that essentially mirrors the initial solidification composition of liquid pools. Therefore, measurement of the composition of NbC precipitate and comparing it with the composition calculated by Thermo-Calc can effectively confirm the source of the precipitate.

For verifying the Thermo-Calc results experimentally, APT experiments were performed to determine the composition of the NbC nano-precipitates, after preparing the samples by FIB and identifying the precipitate locations using TEM (Fig. 10(d)). Results indicate significant aggregation of C and Nb in NbC, while W is absent (Figs. 10 (e1–e4)). To identify NbC and quantify the elemental distributions, a surface with a C concentration of 0.15 at. % is constructed (Fig. 10(f)), and a one-dimensional (1D) composition map perpendicular to this surface is created (Fig. 10(g)). The elemental content in NbC obtained from APT is consistent with the Thermo-Calc predictions (Fig. 10(h)), which confirms the accuracy of non-equilibrium solidification calculations, indicating that NbC originates from the liquid phase. As the temperature reaches the precipitation range for NbC (2680 to 2755 °C), the combination of low  $ \Delta H_{mix} $ and high  $ \Delta G^* $,  $ N_y \leq $ values promotes Nb and C atoms.



<div style="text-align: center;"><img src="imgs/img_in_chart_box_186_112_451_322.jpg" alt="Image" width="22%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_458_110_732_335.jpg" alt="Image" width="23%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_733_114_1006_332.jpg" alt="Image" width="22%" /></div>


<div style="text-align: center;">(d) Diffusion coefficients 3000 2400 1800 1200 600 (K)</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_457_363_734_570.jpg" alt="Image" width="23%" /></div>


<div style="text-align: center;">Fig. 9. Evaluation of the precipitate stability contained in (Nb $ _{15} $Ta $ _{10} $W $ _{75} $) $ _{98.5} $C $ _{1.5} $ RMPEA by comparing (a) mixing enthalpy; Comparative analysis of nucleation and growth ability in BCC phase and NbC based on (b) the driving force for nucleation, (c) the rate of nucleation, and (d) the diffusion coefficient.</div>


<div style="text-align: center;">Intrinsic diffusion coefficients and activation energies for diffusion.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>Nb</td><td style='text-align: center; word-wrap: break-word;'>Ta</td><td style='text-align: center; word-wrap: break-word;'>W</td><td style='text-align: center; word-wrap: break-word;'>C</td><td style='text-align: center; word-wrap: break-word;'>Ref.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \zeta_{0} $ ( $ 10^{-4} $ m $ ^{2} $/s)</td><td style='text-align: center; word-wrap: break-word;'>4.5</td><td style='text-align: center; word-wrap: break-word;'>6.2</td><td style='text-align: center; word-wrap: break-word;'>46</td><td style='text-align: center; word-wrap: break-word;'>2.58</td><td style='text-align: center; word-wrap: break-word;'>[49]</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Q $ _{D} $ (KJ/mol)</td><td style='text-align: center; word-wrap: break-word;'>480.2</td><td style='text-align: center; word-wrap: break-word;'>601.7</td><td style='text-align: center; word-wrap: break-word;'>666.2</td><td style='text-align: center; word-wrap: break-word;'>140.6</td><td style='text-align: center; word-wrap: break-word;'>[49]</td></tr></table>

to rapidly aggregate resulting in the nucleation of NbC from the liquid phase. During LPBF, the added WC particles dissolve into the molten pool first, followed by the distribution of C throughout the liquid alloy, and subsequent precipitation of NbC from the liquid phase upon solidification. This process circumvents the uneven distribution and agglomeration of secondary particles, which is a common phenomenon otherwise [50].

#### 4.2. Effect of the NbC precipitates on the grain structure

To analyze the effects of the in-situ formed NbC on the grain shape, especially on the planes along BD (X-Z and Y-Z), the grain boundary distributions are obtained and plotted in Figs.11 (a₁–a₄). Based on these images, the size of the irregular grains is measured using two different (line intercept and area measurement) methods. The line intercept method measures the average size of grains intersected by a line, while the area measurement method estimates the average grain size based on the grain's area. The equations for these methods are the following [51]:

 $$ \mathbf{d}_{Line}=\frac{1}{N_{g}}\sum_{i=1}^{N_{g}}di $$ 

 $$ \mathrm{d}_{Area}=\frac{2\sum_{i=1}^{Ng}A\mathrm{i}\bullet\left(A\mathrm{i}/\pi\right)^{1/2}}{\sum_{i=1}^{Ng}A\mathrm{i}} $$ 

where  $ d_{line} $ is the average grain size obtained by the line intercept method,  $ N_{g} $ is the total number of grains,  $ d_{i} $ is the length for grain i,  $ d_{Area} $ is the average grain size obtained by the area method,  $ A_{i} $ is the area of grain i, and  $ 2(A_{i}/\pi)^{1/2} $ is the equivalent diameter based on the area of grain i. By comparing grain size values obtained by the line intercept method along the X direction (for the width of columnar grains), along the Z direction (for the length of columnar grains), and by the area method (for the averaged size of columnar grains), the impact of WC particles on the size of the columnar grains could be revealed. The grain size on X-Z plane decrease from  $ 7.34 \pm 1.3 $  $ \mu $m in  $ Nb_{15}Ta_{10}W_{75} $ to  $ 6.10 \pm 0.9 $  $ \mu $m in  $ Nb_{15}Ta_{10}W_{75} $  $ 98.5C_{1.5} $, as shown in Fig. 11(b) (similar trend can be seen for the X-Y plane as well, as shown in Supplementary-Note 4). Figs. 11(c) and (d) show the grain size distributions with the measurement line directions oriented perpendicular or parallel to the Z-axis, respectively. The vertical grain size ( $ 10.4 \mu $m) in  $ Nb_{15}Ta_{10}W_{75} $ exceeds the horizontal one ( $ 6.72 \mu $m), typical of columnar grain morphology. The grain size in  $ Nb_{15}Ta_{10}W_{75} $  $ 98.5C_{1.5} $ decreases to  $ 6.46 \mu $m in the horizontal direction and  $ 5.98 \mu $m in the vertical direction, displaying a much more equiaxed morphology than in  $ Nb_{15}Ta_{10}W_{75} $. These results further confirm that the NbC precipitates not only inhibit the columnar grain growth during LPBF, but also lead to the refinement of the grains.



The influence of NbC and corresponding process parameters on the suppression of columnar grains is analyzed using the inter-dependence model, which effectively evaluates the synergetic effect of alloy composition, nucleation efficiency, and interparticle distance on grain refinement [52,53]. This model has been widely used to evaluate grain size in alloys produced using casting [54], welding [55], and additive manufacturing [56]. The interdependence model and the key control parameters of grain size can be expressed as following [57]:

 $$ d_{gs}=X_{cs}+X_{dl}+X_{sd} $$ 

 $$ X_{cs}=\frac{D\cdot z\Delta T_{n}}{\nu Q} $$ 

 $$ \Delta T_{n}=\frac{C_{E}}{\Delta S_{v}}\delta^{2} $$ 

 $$ Q=\sum_{i=1}^{\mathrm{n}}m_{i}\cdot(k_{i}-1)\cdot C_{0,i} $$ 

 $$ X_{dl}\propto Q $$ 

 $$ X_{\mathrm{sd}}\propto\frac{\Delta T}{\Delta T_{\mathrm{n}}} $$ 

 $$ \Delta T=\Delta T_{cs}+\Delta T_{t} $$ 

<div style="text-align: center;"><img src="imgs/img_in_chart_box_184_112_1005_287.jpg" alt="Image" width="68%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_188_286_1003_515.jpg" alt="Image" width="68%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_185_525_1006_746.jpg" alt="Image" width="68%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_185_744_1006_969.jpg" alt="Image" width="68%" /></div>


<div style="text-align: center;">Fig. 10. (a to c) Predictions and (d to f) experimental verification. (a) Non-equilibrium cooling path containing NbC nano-precipitates. (b) Variations of the volume fractions of different phases with temperature. (c₁–c₄) Element distribution in different phases. (d) An image of the APT samples containing a NbC precipitate. (e₁–e₄) Distribution maps of Nb, Ta, W, and C near and inside NbC. (f) Equal concentration C surface of 0.15 at. % distinguishing the NbC precipitate. (g) 1D concentration map reflecting the element distributions in NbC. (h) Comparison of elemental distributions obtained using experimentally with APT and with the Thermo-Calc based calculations.</div>


 $$ \Delta T_{cs}\propto Q $$ 

 $$ \Delta T_{t}\propto V_{a} $$ 

 $$ V_{a}=v c o s\phi $$ 

where $d_{gs}$ is the grain size predicted using the interdependence model, $X_{cs}$ is the critical distance that grains must grow before producing adequate $\Delta T_{CS}$ to initiate subsequent nuclei, $D$ is the diffusion coefficient of the solute in the liquid, $z$ is the fraction of $\Delta T_{CS}$ required for heterogeneous nucleation, $\nu$ is the laser scanning speed, $\Delta T_{CS}$ is the undercooling of critical nucleation, $C_{E}$ is the elasticity coefficient, $\Delta S\nu$ is the entropy of fusion per unit volume, and $\delta$ is the degree of interfacial lattice parameter match between the nucleating particles and the matrix. $\Delta T_{n}$ is closely related to $\delta$ between nucleating particles and matrix. $A$ smaller $\delta$ lowers $\Delta T_{n}$ is required for the activation of heterogeneous nucleation processes, i.e., $\Delta T_{n} \propto \delta$ [52]. $Q$ is a growth restriction factor; $m_{i}$ is the slope of the liquidus line for the $i^{th}$ solute in the alloy; $k_{i}$ and $C_{0,i}$ are the partition coefficient and solute concentration, respectively. $X_{dl}$ is the diffusion field distance of accumulated solutes that can compensate for insufficient $\Delta T_{CS}$ due to solute diffusion at the S/L interface and is directly related to $Q$ values. $X_{sd}$ is the average distance from $X_{dl}$ to the nearest particle that can effectively nucleate. It is closely related to the effective nucleation particle density and can be evaluated through undercooling. When $\Delta T_{n}$ is lower than the undercooling at the solid/liquid interface ($\Delta T$), numerous heterogeneous nucleation events are activated, reducing $X_{sd}$ and inhibiting columnar grain formation [58]. $X_{sd}$ is positively correlated with $\Delta T$ and negatively correlated with $\Delta T_{n}$ $\Delta T$ is composed of $\Delta T_{CS}$ and thermal undercooling ($\Delta T_{l}$) under non-equilibrium solidification conditions [58]. $\Delta T_{CS}$ is primarily associated with the solute segregation occurring ahead of the solid/liquid interface and can be quantitatively evaluated using $Q$ [25]. $\Delta T_{l}$ is the thermal undercooling when the actual growth rate ($V_{a}$) at the solid/liquid interface lags behind the theoretical pull rate ($V_{theo}$) induced by the high cooling rate that prevails during LPBF [58]. Generally, $V_{a}$ is directly correlated with laser scanning speed $\nu$ [53]. $\varphi$ is the angle ($\degree$)



<div style="text-align: center;"><img src="imgs/img_in_image_box_186_110_999_620.jpg" alt="Image" width="68%" /></div>


<div style="text-align: center;">Fig. 11. EBSD data for  $ Nb_{15}Ta_{10}W_{75} $ and  $ (Nb_{15}Ta_{10}W_{75})_{98.5}C_{1.5} $.  $ (a_1-a_4) $ Grain boundary distribution maps used to measure irregular grain size. (b) Average grain sizes measured by the area method. (c) Horizontal grain sizes and (d) Vertical grain sizes measured by the line intercept method.</div>


between the  $ V_a $ and  $ \nu $ directions. The degree of  $ \Delta T_t $ is controlled by the values of  $ \nu $. As the value of  $ \nu $ increases, the delay between  $ V_a $ and  $ V_{theo} $ becomes more pronounced, resulting in a larger  $ \Delta T_t $.

The comparative evaluation of the solidification distance and undercooling illustrates the inhibitory effect of adding WC to RHEA and the resulting NbC precipitates on the columnar grains, as shown in Fig. 12. The incorporation of WC and the presence of NbC reduces  $ X_{GS} $ for three reasons. First, NbC being coherent with the matrix (Fig. 7(e1)) reduces  $ \Delta T_n $ and shortens  $ X_{GS} $. Second, WC powder markedly improves the laser absorptivity (Fig. 2(d2)) and increases  $ \nu $ (Section 3.1), resulting in the shortening of  $ X_{GS} $. Third, C that is released through the dissolution of WC increases Q of (Nb $ _{15} $Ta $ _{10} $W $ _{75} $) $ _{98.5} $C $ _{1.5} $ (Table 3), further reducing  $ X_{GS} $. Therefore, (Nb $ _{15} $Ta $ _{10} $W $ _{75} $) $ _{98.5} $C $ _{1.5} $ exhibits a smaller  $ X_{GS} $ compared to  $ Nb_{15} $Ta $ _{10} $W $ _{75} $. The  $ X_{d1} $ term of (Nb $ _{15} $Ta $ _{10} $W $ _{75} $) $ _{98.5} $C $ _{1.5} $ is slightly smaller.

<div style="text-align: center;">Growth restriction factors and related calculation parameters for i th solutes.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>m</td><td style='text-align: center; word-wrap: break-word;'>k</td><td style='text-align: center; word-wrap: break-word;'>Q</td><td style='text-align: center; word-wrap: break-word;'>Ref.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Nb</td><td style='text-align: center; word-wrap: break-word;'>3.4</td><td style='text-align: center; word-wrap: break-word;'>1.08</td><td style='text-align: center; word-wrap: break-word;'>0.27</td><td style='text-align: center; word-wrap: break-word;'>[17]</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Ta</td><td style='text-align: center; word-wrap: break-word;'>16.5</td><td style='text-align: center; word-wrap: break-word;'>1.48</td><td style='text-align: center; word-wrap: break-word;'>8.0</td><td style='text-align: center; word-wrap: break-word;'>[17]</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>W</td><td style='text-align: center; word-wrap: break-word;'>15.1</td><td style='text-align: center; word-wrap: break-word;'>2.50</td><td style='text-align: center; word-wrap: break-word;'>22.7</td><td style='text-align: center; word-wrap: break-word;'>[17]</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>C</td><td style='text-align: center; word-wrap: break-word;'>-55</td><td style='text-align: center; word-wrap: break-word;'>$ \rightarrow $0</td><td style='text-align: center; word-wrap: break-word;'>55</td><td style='text-align: center; word-wrap: break-word;'>[17]</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Nb $ _{15} $Ta $ _{10} $W $ _{75} $</td><td style='text-align: center; word-wrap: break-word;'>/</td><td style='text-align: center; word-wrap: break-word;'>/</td><td style='text-align: center; word-wrap: break-word;'>17.82</td><td style='text-align: center; word-wrap: break-word;'>This work</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>(Nb $ _{15} $Ta $ _{10} $W $ _{75} $) $ _{98.5} $C $ _{1.5} $</td><td style='text-align: center; word-wrap: break-word;'>/</td><td style='text-align: center; word-wrap: break-word;'>/</td><td style='text-align: center; word-wrap: break-word;'>18.38</td><td style='text-align: center; word-wrap: break-word;'>This work</td></tr></table>

than that of  $ Nb_{15}Ta_{10}W_{75} $ due to higher Q. The presence of NbC also reduces  $ X_{sd} $. The coherency between NbC and the matrix also helps reduce  $ \Delta T_{n} $ required for heterogeneous nucleation. In  $ Nb_{15}Ta_{10}W_{75} $,

<div style="text-align: center;">(a)</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_186_1034_1002_1410.jpg" alt="Image" width="68%" /></div>


<div style="text-align: center;">Fig. 12. Schematic illustrations of the generation of the undercooling including  $ \Delta T_b $  $ \Delta T_c $ and the solidification distance including  $ X_{cs} $  $ X_{db} $  $ X_{sd} $ in (a)  $ Nb_{15}Ta_{10}W_{75} $ and (b)  $ Nb_{15}Ta_{10}W_{75} $ 98.5  $ C_{1.5} $, illustrating the inhibitory effect of adding WC powder and optimizing process parameters on columnar grains. The schematic illustration is not drawn to scale and is intended for illustrative purposes; actual undercooling and solidification distances may have deviations.</div>


heterogeneous nucleation primarily occurs on the native nuclei particles, such as impurities or oxides that may be present in the melt pool. Such nuclei are usually incoherent with the matrix, characterized by relatively high δ, leading to larger ΔTₙ [52]. Besides, the incorporation of the WC powders into Nb₁₅Ta₁₀W₇₅ increases ΔTₛ owing to the presence of C in solution, which has a high Q value (Table 3). Simultaneously, the added WC powder significantly enhances the laser absorptivity in (Nb₁₅Ta₁₀W₇₅)₉₈,₅C₁.₅, thereby increasing ν (Section 3.1) and ultimately increasing the degree of ΔTₜ. The incorporation of WC and the presence of in-situ NbC nano-precipitates reduce ΔTₙ while increase ΔT, meeting the nucleation condition of ΔT ≥ ΔTₙ, which, in turn, shortens Xₛd for (Nb₁₅Ta₁₀W₇₅)₉₈,₅C₁.₅. In conclusion, the above theoretical analysis made on the basis of the interdependence model indicates that adding WC powder and the in-situ NbC formation reduces Xₛs, Xₑ, and Xₛd, which effectively inhibit the columnar grain growth in (Nb₁₅Ta₁₀W₇₅)₉₈,₅C₁.₅. Moreover, driven by the combination of low ΔHₘₐₓ and high ΔG*, Nₛ, ₛ values, NbC particles re-precipitate from the liquid phase and are uniformly distributed, which serves as heterogeneous nucleation sites and pin grain boundaries (preventing grain coarsening) during repeated heating that solidified layers undergo during LPBF [52].

#### 4.3. Effect of NbC on the mechanical properties at room temperature

The anisotropy of the mechanical properties at KI is mainly controlled by grain morphology [15]. Both as-fabricated  $ Nb_{15}Ta_{10}W_{75} $ and  $ Nb_{15}Ta_{10}W_{75}98.5C_{1.5} $ exhibit a high relative density of above 99.2 % (Fig. 3), which minimizes the potential influence of porosity on mechanical properties and anisotropy [60,61]. The formation of NbC nano-precipitates in the  $ Nb_{15}Ta_{10}W_{75}98.5C_{1.5} $ effectively reduces anisotropy. During the manufacturing of  $ Nb_{15}Ta_{10}W_{75} $ using the LPBF technique, the presence of a steep thermal gradient promotes grain growth towards the melt pool core [16], ultimately forming a microstructure with columnar grains that are parallel to the Z-axis (Figs. 5 (c2) and (d1)). When the alloy is stressed along the Z-axis, they align with the long axis of the columnar grains (Figs. 5 (c2) and (d1)). The straight boundaries of the columnar grains along their long axis promote crack propagation during plastic deformation [59], resulting in poor compressibility and strength of 2.6 % and 759 MPa, respectively. In contrast, forces applied along the X-axis are parallel to the short axis of the columnar grains (Figs. 5 (c2) and (d1)). Compared to long-axis columnar GBs, short-axis curved boundaries effectively hinder crack propagation [59], enhancing compressibility (5.3 %) and strength (1409 MPa). The incorporation of WC powder into  $ Nb_{15}Ta_{10}W_{75} $ induces the NbC precipitates (Fig. 7) and changes the grain morphology to an equiaxed one (Figs. 5 (c4) and (d2)). As a result, the mechanical anisotropy is reduced substantially. In addition, NbC enhances the RT mechanical properties. For  $ Nb_{15}Ta_{10}W_{75} $ and  $ Nb_{15}Ta_{10}W_{75}98.5C_{1.5} $, the contributions from solid-solution hardening ( $ \Delta\sigma_{SSH} $), grain boundary strengthening ( $ \Delta\sigma_{GB} $), dislocation strengthening ( $ \Delta\sigma_{DIS} $), and precipitation strengthening ( $ \Delta\sigma_{p} $) to the total yield strength ( $ \sigma_{y} $) can be estimated using the following relations [62–64]:

 $$ \sigma_{\mathrm{y}}=\Delta\sigma_{0}+\Delta\sigma_{\mathrm{S S H}}+\Delta\sigma_{\mathrm{G B}}+\Delta\sigma_{\mathrm{D I S}}+\Delta\sigma_{\mathrm{p}} $$ 

 $$ \Delta\sigma_{0}=\sum x_{i}\sigma_{i} $$ 

 $$ \Delta\sigma_{GB}=Kd^{-1/2} $$ 

 $$ \Delta\sigma_{\mathrm{D I S}}=M\alpha\mu b\rho^{1/2} $$ 

 $$ \Delta\sigma_{\mathrm{p}}=0.26\frac{\mu b}{r}f^{1/2}\ln\left(\frac{r}{b}\right) $$ 

where  $ \Delta\sigma_0 $ is the lattice friction stress of the matrix which is estimated using the weighed average of the lattice friction stresses ( $ \sigma_f $) of the constituent pure metals [64], k is the Hall-Petch slope (210 MPa·μm¹/² for refractory metals [64]), d is the average grain size (estimated using the area method on the EBSD data obtained on the X-Z plane (Fig. 11(b)), M is the Taylor factor (~2.733 for BCC refractory metals) [64],  $ \alpha $ is an empirically determined constant (0.5 for BCC metals [64]),  $ \mu $ is the shear modulus calculated according to the mixed weighting equation [29], and  $ \rho $ is obtained from the XRD analysis (Fig. 4). Since dislocations cannot cut through the NbC particles because of their large size (>37 nm) [63], the Orowan looping mechanism is the primary precipitation-strengthening mechanism [63], which was used to estimate  $ \Delta\sigma_p $ for (Nb₁₅Ta₁₀W₇₅)₉₈.₅C₁.₅. Due to the rapid cooling rates and the small melt pool sizes associated with the LPBF process, it is difficult for solutes and solute atoms to rapidly diffuse and generate concentration gradient over a larger length scale (of micrometer level) [13] [65]. The Toda-Caraballo model can evaluate the solid-solution hardening effect of RMEPEAs fabricated using the LPBF process [66]. This model overcomes the difficulty of distinguishing "solute-solvent" in the high entropy alloys, and utilizes a matrix to calculate lattice distortion caused by a small amount of component fluctuations, which is consistent with the atomic diffusion behavior under non-equilibrium conditions.  $ \Delta\sigma_{SSH} $ was assumed to be the same for Nb₁₅Ta₁₀W₇₅ and (Nb₁₅Ta₁₀W₇₅)₉₈.₅C₁.₅, as all the added C precipitates out in the form of NbC.



The contributions of the different strengthening mechanisms to  $ Nb_{15}Ta_{10}W_{75} $ and  $ (Nb_{15}Ta_{10}W_{75})_{98.5}C_{1.5} $ at RT are shown in Fig. 13. Their sum, being close to  $ \sigma_{y} $ obtained from the experiment, renders reasonable validity to the methods employed for the estimation.  $ \Delta\sigma_{0} $ and  $ \Delta\sigma_{SSH} $ are the primary contributors to the strength of  $ Nb_{15}Ta_{10}W_{75} $, providing 430 and 337 MPa respectively, which correspond to 32.9 % and 25.8 % of  $ \sigma_{y} $ [64], respectively.  $ \sigma_{i} $ of Nb, Ta, and W are 240, 189, and 550 MPa, respectively. The high proportion of W content in  $ Nb_{15}Ta_{10}W_{75} $ significantly enhances  $ \Delta\sigma_{0} $, contributing substantially to  $ \sigma_{y} $. The severe lattice distortion significantly improves  $ \Delta\sigma_{SSH} $ [29], thereby positively contributing to  $ \sigma_{y} $.

In  $ (Nb_{15}Ta_{10}W_{75})_{98.5}C_{1.5} $, both  $ \Delta\sigma_0 $ and  $ \Delta\sigma_{SSH} $ continue to be the major strengthening contributors, accounting for 28.3 % and 22.2 % of  $ \sigma_y $, respectively. The strengthening effect of these mechanisms does not vary because of negligible variations in the matrix composition. However, the NbC precipitates generated during LPBF of  $ (Nb_{15}Ta_{10}W_{75})_{98.5}C_{1.5} $ can pin GBs (from coarsening during the thermal cycles of LPBF) and dislocations, thereby refining grains (Fig. 11) and increasing  $ \rho $ (Fig. 4). Benefiting from these microstructural modifications,  $ \Delta\sigma_{GB} $ and  $ \Delta\sigma_{DIS} $ increase to 269 and 313 MPa, respectively. Moreover, the NbC precipitates themselves can also enhance the strength by hindering the dislocation mobility, contributing an additional 167 MPa. Thus, the enhanced strength of  $ (Nb_{15}Ta_{10}W_{75})_{98.5}C_{1.5} $ mainly arises from the combination of  $ \Delta\sigma_{GB} $,  $ \Delta\sigma_{DIS} $, and  $ \Delta\sigma_p $.

Furthermore,  $ (Nb_{15}Ta_{10}W_{75})_{98.5}C_{1.5} $ exhibits superior plasticity (8.3%) compared to  $ Nb_{15}Ta_{10}W_{75} $ (5.3%), despite comparable dislocation densities in them (Section 3.2). The higher plasticity is also reflected in the fracture morphologies (Figs.8 (b_3-b_4)). This difference in the plastic deformability between the two alloys examined is mainly due to the differences in microstructure. Specifically,  $ (Nb_{15}Ta_{10}W_{75})_{98.5}C_{1.5} $ contains a higher population of LAGBs than  $ Nb_{15}Ta_{10}W_{75} $ (Figs.11(a_2) and (a_4)), which is caused by the pinning effect of precipitates on grain boundaries (Fig. 6). The high proportion of LAGBs can blunt the crack tips and hinder crack propagation [59], and bear a larger degree of deformation before fracture by homogenizing the strain [60], ultimately improving plasticity and transforming fracture mechanism from partial cleavage to quasi-cleavage.

#### 4.4. Effect of the nano-precipitates on HT mechanical properties

Fig.14(a) compares the HT strengths of Nb₁₅Ta₁₀W₇₅ and (Nb₁₅Ta₁₀W₇₅)₉₈.₅C₁.₅ with those of other RHEAs reported in literature [67–73]. It shows (Nb₁₅Ta₁₀W₇₅)₉₈.₅C₁.₅ exceeds all the others at

<div style="text-align: center;"><img src="imgs/img_in_chart_box_188_114_1004_494.jpg" alt="Image" width="68%" /></div>


<div style="text-align: center;">Fig. 13. Comparison of  $ Nb_{15}Ta_{10}W_{75} $ versus  $ (\mathrm{Nb}_{15}\mathrm{Ta}_{10}\mathrm{W}_{75})_{98.5}\mathrm{C}_{1.5} $ in terms of strengthening mechanisms contributions and proportions.</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_189_577_1003_987.jpg" alt="Image" width="68%" /></div>


<div style="text-align: center;">Fig. 14. A comparison of the (a) HT strengths and (b) softening temperatures and atomic mismatch of various RMPEAs with those examined in this study.</div>


various testing temperatures. The softening temperature ( $ T_{c} $) and atomic mismatch degree ( $ \delta_{r} $) are important aspects of HT strength of alloys and hence can serve as the critical parameters for evaluation [29]. As the temperature is increased, a transition in the dominant deformation mechanism—from screw to edge dislocation mobility dominated regimes—occurs, and  $ T_{c} $ reflects this transition temperature range (usually 0.3–0.5 times melting temperature) [74,75]. A higher  $ T_{c} $ is beneficial for maintaining strength at higher temperatures.  $ \delta_{r} $ reflects the degree of lattice mismatch and is related to the resistance of dislocation movement at HT, and can be estimated using the following equation:

 $$ \delta_{r}=100\sqrt{\sum_{i=1}^{n}c_{i}\left(1-\frac{r_{i}}{\sum_{i=1}^{n}c_{i}r_{i}}\right)^{2}} $$ 

where $c_i$ is the atomic fraction of the $i^\text{th}$ element and $r_i$ is the atomic radius. Fig.14(b) compares the values of $T_c$ and $\delta_r$ of Nb$_{15}$Ta$_{10}$W$_{75}$ and (Nb$_{15}$Ta$_{10}$W$_{75}$)$_{98.5}$C$_{1.5}$ with the respective values reported for other RMPEAs. It is observed that (Nb$_{15}$Ta$_{10}$W$_{75}$)$_{98.5}$C$_{1.5}$ has the highest $T_c$ and $\delta_r$ values, consistent with its superior HT strength.

The impact of NbC on the HT properties is evaluated by analyzing the work-hardening rates and dislocation types at different compression temperatures. The work-hardening curves, classified into two types (Figs.15 (a1) and (a2)), reveal distinct behaviors based on the compression temperature. Below 1400 °C, the work hardening curves of Nb$_{15}$Ta$_{10}$W$_{75}$ and (Nb$_{15}$Ta$_{10}$W$_{75}$)$_{98.5}$C$_{1.5}$ exhibit high work-hardening rates, indicating strong HT softening resistance. Above 1400 °C, the work hardening behavior shows a significant transformation, with a sharp decrease in hardening rate with true strain in stage I ($\varepsilon_T < 10\%$), indicating that dislocation slip occurs readily at this temperature. Besides, (Nb$_{15}$Ta$_{10}$W$_{75}$)$_{98.5}$C$_{1.5}$ exhibits a lower slope in the work-hardening curve ($K_{WH}$) than Nb$_{15}$Ta$_{10}$W$_{75}$, indicating stronger resistance to HT deformation. The difference in work-hardening ability is closely related to temperature and micro-deformation mechanisms. To this end, the phase type and $\rho$ of compressed samples subjected to $\varepsilon_T = 10\%$ at 1400 and 1600 °C are evaluated using XRD, as shown in Fig. 15(b). NbC nano-precipitates still exist in (Nb$_{15}$Ta$_{10}$W$_{75}$)$_{98.5}$C$_{1.5}$ after undergoing HT compression with $\varepsilon_T = 10\%$, which is beneficial for HT strength. The value of $\rho$, estimated using the Scherrer formula, in (Nb$_{15}$Ta$_{10}$W$_{75}$)$_{98.5}$C$_{1.5}$ is higher than that in Nb$_{15}$Ta$_{10}$W$_{75}$ after HT



<div style="text-align: center;"><img src="imgs/img_in_chart_box_159_109_462_331.jpg" alt="Image" width="25%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_463_110_751_320.jpg" alt="Image" width="24%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_757_110_1029_320.jpg" alt="Image" width="22%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_223_343_1011_664.jpg" alt="Image" width="66%" /></div>


<div style="text-align: center;">Fig. 15. Work hardening rate curves for (a₁) Nb₁₅Ta₁₀W₇₅ and (a₂) (Nb₁₅Ta₁₀W₇₅)₉₈.₅C₁.₅ at different compression temperatures; (b) Phase structure, ρ and d of samples compressed at 1400 °C and 1600 °C with εₜ = 10 % detected by XRD test; BF TEM images of dislocation types in deformed samples with εₜ = 10 %: Nb₁₅Ta₁₀W₇₅ compressed at (c₁) 1400 °C and (c₂) 1600 °C, (Nb₁₅Ta₁₀W₇₅)₉₈.₅C₁.₅ compressed at (c₃) 1400 °C and (c₄) 1600 °C.</div>


compression (Table 4), which benefits the HT strength [76].

Furthermore, the type of dislocation dominating the deformation plays a critical role in determining the HT strength [75]. The maximum  $ T_c $ of both  $ Nb_{15}Ta_{10}W_{75} $ and  $ (Nb_{15}Ta_{10}W_{75})_{98.5}C_{1.5} $ is about 1500 °C. Thus, the compression temperature of 1600 °C marks the transition between dislocation types. At temperatures below  $ T_c $, work-hardening curves dominated by the screw dislocations show continuous deformation behavior, while deformation dominated by the edge dislocations at temperatures above  $ T_c $ results in a rapid decrease in the hardening rate [77]. The observed hardening curve conforms to such a change in the pattern, supporting the hypothesis that the HT strength transitions from screw-dominated to edge-dominated dislocation motion. To further clarify the types of dislocations operating at different temperatures, two-beam BF TEM images are obtained from compressed samples subjected to  $ \varepsilon_T = 10\% $ at 1400 and 1600 °C. Results are shown in Figs.15 ( $ c_1-c_4 $). The g vector is marked in each image, and its direction is denoted by a white arrow. b is determined using the  $ g \times b = 0 $ condition; detailed information is provided in Supplementary-Note 5 of supplementary material.  $ (Nb_{15}Ta_{10}W_{75})_{98.5}C_{1.5} $ shows more dislocation lines than  $ Nb_{15}Ta_{10}W_{75} $, consistent with the higher  $ \rho $ results obtained using XRD. The dislocations are colored according to their respective orientation relationships with b. It is found that there are two kinds of dislocations based on their orientation relationship with different  $ b: \pm 1/2[11-1] $ in red, and  $ \pm 1/2[001] $,  $ \pm 1/2[111] $,  $ \pm 1/2[1-11] $ in orange. It is observed that only the edge dislocations exist in the  $ Nb_{15}Ta_{10}W_{75} $ and  $ (Nb_{15}Ta_{10}W_{75})_{98.5}C_{1.5} $ samples compressed to  $ \varepsilon_T $ of 10 % at 1400 °C. In contrast, both screw and edge dislocations coexist in the samples that

##### Table 4

<div style="text-align: center;">The  $ \rho $ values of samples compressed at  $ 1400\,^{\circ}\mathrm{C} $ and  $ 1600\,^{\circ}\mathrm{C} $ with  $ \varepsilon_{T}=10\% $.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td colspan="2">$ \text{Nb}_{15}\text{Ta}_{10}\text{W}_{75} $</td><td colspan="2">$ (\text{Nb}_{15}\text{Ta}_{10}\text{W}_{75})_{98.5}\text{C}_{1.5} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1400℃</td><td style='text-align: center; word-wrap: break-word;'>1600℃</td><td style='text-align: center; word-wrap: break-word;'>1400℃</td><td style='text-align: center; word-wrap: break-word;'>1600℃</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \rho $ ( $ 10^{14}/\text{m}^{2} $)</td><td style='text-align: center; word-wrap: break-word;'>8.35</td><td style='text-align: center; word-wrap: break-word;'>5.35</td><td style='text-align: center; word-wrap: break-word;'>9.67</td><td style='text-align: center; word-wrap: break-word;'>5.71</td></tr></table>

were compression tested at 1600 °C ( $ \varepsilon_T = 10\% $). The accumulation of dislocations at the GBs, which is also observed, increases the back stress that could hinder dislocation glide. The average dislocation velocity ( $ \nu_d $) is estimated using the Orowan equation [78,79]:

 $$ \mathbf{v}_{\mathrm{d}}=\frac{\varepsilon_{v}}{\rho b} $$ 

 $$ \varepsilon_{v}=\frac{\varepsilon_{L}}{H} $$ 

where $\rho$ is obtained from the XRD results (see Table 4), $\epsilon_v$ is the strain rate, $H$ is the height of the HT compressed sample, $\epsilon_L$ is a constant loading rate of HT compression. At temperatures below $T_c$, only pure edge dislocations survived in the compressed samples $Nb_{15}Ta_{10}W_{75}$ and $\left(Nb_{15}Ta_{10}W_{75}\right)_{98.5}C_{1.5}$. This is because of the difficulty of screw dislocation cores dissociating into nonplanar structures during motion, while edge dislocations tend to divide into segments that slip more easily along the glide planes [72]. Therefore, screw dislocations are more prone to annihilation than edge dislocations, leading to the survival of pure edge dislocations and dominating the slip rate and HT strength. The estimated velocity of screw dislocations $\left(v_d\right)$ in $\mathrm{Nb}_{15}\mathrm{Ta}_{10}\mathrm{W}_{75}$ and $\left(Nb_{15}\mathrm{Ta}_{10}W_{75}\right)_{98.5}C_{1.5}$ compressed at $1400\,^\circ\mathrm{C}$ are $1.51$ and $1.30\,\mathrm{mm/s}$, respectively. When the temperature exceeds $T_c$, numerous Frank-Read sources are activated for dislocation multiplication, promoting the glide of the screw dislocations, whereas edge dislocations are less influenced. With deformation, the speed of screw dislocations becomes comparable to those of edge dislocations ($\nu_{de}$), consequently maintaining the HT strength. The screw and edge dislocations in $\mathrm{Nb}_{15}\mathrm{Ta}_{10}W_{75}$ and $\left(Nb_{15}\mathrm{Ta}_{10}W_{75}\right)_{98.5}C_{1.5}$ at $1600\,^\circ\mathrm{C}$ have similar mobilities, with $\nu_{ds} = \nu_{de} = 2.36\,\mathrm{mm/s}$ for $\mathrm{Nb}_{15}\mathrm{Ta}_{10}W_{75}$ and $\nu_{ds} = \nu_{de} = 2.21\,\mathrm{mm/s}$ for $\left(Nb_{15}\mathrm{Ta}_{10}W_{75}\right)_{98.5}C_{1.5}$. The HT strength of $\left(Nb_{15}\mathrm{Ta}_{10}W_{75}\right)_{98.5}C_{1.5}$ increases by about $111\,\mathrm{MPa}$ at $1400\,^\circ\mathrm{C}$ and $110\,\mathrm{MPa}$ at $1600\,^\circ\mathrm{C}$ compared to $\mathrm{Nb}_{15}\mathrm{Ta}_{10}W_{75}$, attributed to the impediment of screw/edge dislocation movement by the NbC particles. Based on these results, it can be concluded that the NbC nano-precipitates can stably survive at HT and

effectively impede screw/edge dislocation movement at HT, leading to higher  $ \rho $ and improved HT strength.

### 5. Summary and conclusions

A design strategy for composite RMPEAs, suitable for LPBF via ceramic powder addition and in-situ nano-precipitate formation, was developed to simultaneously enhance printability, reduce anisotropy, and sustain strength at HT conditions. The main conclusions of this study are the following.

2) Incorporating 1.5 at. % WC powder also enhanced the laser absorptivity from 71 % to 86 % without compromising powder flowability, expanding printing ranges of about 50 Jmm $ ^{-3} $, reducing LOF pores, and improves the printed part density from 99.2 ± 0.15 % to 99.5 ± 0.1 %.

1) By estimating the solid solubility and critical re-precipitation amounts of the in-situ nano-precipitates, and measuring the powder flowability and laser absorptivity, we found that adding 1.5 at. % WC powder to matrix powders promotes the formation of in-situ phase and improves the print quality.

3) During LPBF, the added WC powder particles dissolve in the melt pool and the C combines with Nb to form NbC in-situ. These precipitates, subsequently, act as heterogeneous nucleates to shorten solidification distance and inhibit columnar grain growth. As a result, a substantial reduction in microstructural and mechanical anisotropy is obtained. Moreover,  $ (\mathrm{Nb}_{15}\mathrm{Ta}_{10}\mathrm{W}_{75})_{98.5}\mathrm{C}_{1.5} $ exhibits a superior yield strength at RT, which is attributed to the grain boundary, dislocation, and precipitation strengthening mechanisms. The HT strength of  $ (\mathrm{Nb}_{15}\mathrm{Ta}_{10}\mathrm{W}_{75})_{98.5}\mathrm{C}_{1.5} $ also increased due to the suppression of dislocation mobility by the NbC nano-precipitates.

### CRediT authorship contribution statement

Ran Duan: Writing – review & editing, Writing – original draft, Validation, Methodology, Data curation. Yakai Zhao: Writing – review & editing, Validation, Supervision. Xiaodan Li: Resources, Methodology. Jintao Xu: Validation, Investigation. Meng Qin: Validation, Investigation, Data curation. Kai Feng: Writing – review & editing, Project administration, Methodology, Funding acquisition, Conceptualization. Zhuguo Li: Resources, Project administration, Methodology, Funding acquisition. Beibei Xu: Visualization, Validation, Software, Resources, Formal analysis, Data curation. Upadrasta Ramamurty: Writing – review & editing, Supervision, Methodology, Investigation, Formal analysis, Data curation, Conceptualization.