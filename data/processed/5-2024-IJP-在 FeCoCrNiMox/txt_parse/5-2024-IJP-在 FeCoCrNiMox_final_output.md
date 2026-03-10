# Multiscale plastic deformation in additively manufactured FeCoCrNiMo $ _{x} $ high-entropy alloys to achieve strength–ductility synergy at elevated temperatures

<div style="text-align: center;"><img src="imgs/img_in_image_box_897_290_953_347.jpg" alt="Image" width="5%" /></div>


Danyang Lin $ ^{a} $, Jixu Hu $ ^{a} $, Renhao Wu $ ^{b,*} $, Yazhou Liu $ ^{a,d} $, Xiaoqing Li $ ^{c} $, Man Jae SaGong $ ^{b} $, Caiwang Tan $ ^{a} $, Xiaoguo Song $ ^{a,*} $, Hyoung Seop Kim $ ^{b,d,e,f,*} $

 $ ^{a} $ State Key Laboratory of Precision Welding & Joining of Materials and Structures, Harbin Institute of Technology, Harbin 150001, China

 $ ^{b} $ Graduate Institute of Ferrous & Eco Materials Technology, Pohang University of Science & Technology, Ponang 3/673, Korea

 $ ^{c} $ Department of Materials Science and Engineering, Applied Materials Physics, KTH - Royal Institute of Technology, Stockholm SE-10044, Sweden

 $ ^{d} $ Department of Materials Science & Engineering, Pohang University of Science & Technology, Pohang 37673, Korea

 $ ^{e} $ Advanced Institute for Materials Research (WPI-AIMR), Tohoku University, Sendai 980-8577, Japan

 $ ^{1} $Institute for Convergence Research and Education in Advanced Technology, Yonsei University, Seoul 03722, South Korea

#### ARTICLE INFO

Keywords:

Additively manufactured FeCoCrNiMo $ _{x} $

Multiscale plastic deformation

Deformation twinning

Molecular dynamics simulation

Elevated temperature

### A B S T R A C T

The application of structural metals in extreme environments necessitates materials with superior mechanical properties. Mo-doped FeCoCrNi high-entropy alloys (HEAs) have emerged as potential candidates for use in such demanding environments. This study investigates the high-temperature performance of FeCoCrNiMoₓ HEAs with varying Mo contents (x = 0, 0.1, 0.3, and 0.5) prepared by laser powder bed fusion additive manufacturing. The mechanical properties were evaluated at room and 600 °C temperatures, and the microstructures were characterized using scanning electron microscopy, electron backscatter diffraction, energy dispersive X-ray spectroscopy, and transmission electron microscopy. The intrinsic dislocation cell patterning, solid-solution strengthening, nanoprecipitation, and twinning effects collectively modulated the plastic deformation behavior of the samples. The high-temperature mechanical performance was comprehensively analyzed in conjunction with ab initio calculations and molecular dynamics simulations to reveal the origin of the experimentally observed strength–ductility synergy of FeCoCrNiMo₀.₃. This study has significant implications for FeCoCrNiMoₓ HEAs and extends our understanding of the structural origins of the exceptional mechanical properties of additively manufactured HEAs.

### 1. Introduction

The pursuit of advanced structural metals that perform reliably in high-temperature environments remains a challenge. High-

entropy alloys (HEAs) have significantly broadened the compositional space of metals owing to their unique physical, chemical, and mechanical properties. Face-centered cubic (FCC) FeCoCrNi-based HEAs exhibit excellent mechanical properties, including high strength, hardness, and wear resistance. (Beyr amali Kivy and Asle Zaeem, 2017; He et al., 2018). The most renowned variant, equiatomic FeCoCrNiMn (Shahmir et al., 2023), tends to form with a low stacking fault energy (SFE) of  $ \sim $20 mJ/m $ ^2 $ (Huang et al., 2015). $ ^{1} $

However, despite the satisfactory mechanical properties of single-phase FeCoCrNi-based HEAs at room and low temperatures (Gludovatz et al., 2014; Kuzminova et al., 2021; Liu et al., 2017), the high-temperature mechanical performance requires further improvement. For instance, Liao et al. (2023) explored the compression behavior of equimolar FeCoCrNi HEAs, and noticed a softening effect at elevated temperatures owing to increased grain boundary migration and thermal activation of the matrix. This pronounced softening effect significantly reduces the strength and plasticity of FeCoCrNi-based HEAs at 600 °C (Lin et al., 2022). During deformation, nanoclusters cause cracks to form at the grain boundaries, leading to a loss of ductility at high temperatures. Similarly, the high-temperature tensile properties of FeCoCrNiMn show evident softening at 600–700 °C, resulting in poor performance at high temperatures (Jo et al., 2022; Sun et al., 2022).

To enhance the high-temperature mechanical properties of HEAs, significant progress has been made in controlling precipitation (Yang et al., 2020) and alloying-element segregation at grain boundaries (Hou et al., 2022). Gan et al. (2024) introduced D022 nanoparticles into an FCC HEA, which increased the dislocation storage capability and strain hardening, greatly improving the tensile properties in the 600–700 °C range. Researchers have also achieved improvements in strength and plasticity at 750 °C by doping the FCC matrix with elements such as Ti, Nb, Ta, Mo, and W to reduce the SFE and introduce nanoscale L12 precipitates, resulting in various work-hardening behaviors (Gao et al., 2024). Therefore, adding trace elements and introducing nanoscale precipitates into the FCC matrix is a promising strategy for improving the high-temperature performance.

The addition of medium-atomic-size Mo to the FeCoCrNi matrix can induce precipitation strengthening in the solid-solution FCC phase and even trigger a eutectic precipitation reaction (Guo et al., 2020). Consequently, Mo-doped FeCoCrNi HEAs exhibit enhanced mechanical properties, including good wear resistance (Fan et al., 2024), corrosion resistance (Dai et al., 2020; Yen et al., 2024), and biocompatibility (Hiyama et al., 2024). By controlling the Mo content, phase selection can be achieved to alter the structure and properties of the HEAs, which is crucial for regulating the performance.

Dai et al. (2021) reported the effect of grain size on the mechanical properties of FeCoCrNiMo₀.₁. The mechanical performance at −196.15 °C was superior to that at 0 °C because of twinning-induced plasticity. By comparison, FeCoCrNiMo₀.₂ has a higher activation energy, and the matrix and precipitate phases segregate during deformation at elevated temperatures (Wu et al., 2018). The enhanced slip reversibility is attributed to improved slip planarity owing to the addition of Mo, which results in a decreased SFE and increased lattice friction stress and shear modulus. Moreover, the stacking-fault-mediated deformation mechanism in FeCoCrNiMo₀.₂ helps to inhibit fatigue-induced plastic deformation (Li et al., 2019). Cai et al. (2017) discovered that Mo-rich intermetallic compounds precipitate in FeCoCrNiMo₀.₂ upon annealing. However, the bonding force between the intermetallic compounds and matrix is weak, and the probability of stacking faults is reduced, thus suppressing the formation of deformation twins and resulting in a tradeoff between strength and ductility. Liu et al. (2016) found that in FeCoCrNiMo₀.₃, the precipitation of hard σ and μ phases greatly strengthens the material (tensile strength of up to 1.2 GPa) without causing severe embrittlement. Shun et al. (2012) reported that with an increase in the Mo content in cast FeCoCrNiMoₓ, the strength increases, whereas the plasticity decreases. Aged FeCoCrNiMo₀.₈ has a higher hardness than aged FeCoCrNiMo₀.₃ and FeCoCrNiMo₀.₅ owing to the precipitation of a larger volume fraction of hard needle-like σ phases in the FCC matrix. However, these studies mostly focused on the influence of Mo on the mechanical properties, without considering the effect of temperature in detail. In particular, few studies have evaluated the high-temperature mechanical properties and microstructural evolution of FeCoCrNiMoₓ HEAs (Li et al., 2022; Wang et al., 2017), and systematic and in-depth studies on the high-temperature mechanical properties and intrinsic deformation mechanisms of FeCoCrNiMoₓ HEAs are lacking.

Laser-based additive manufacturing (L-AM) is an advanced precision manufacturing technique that facilitates high-throughput fabrication and offers significant opportunities for in situ materials design with tailored microstructures (Li et al., 2022). An et al. (2023) revealed that L-AM-processed FCC metals have hierarchical microstructures that exhibit several plastic deformation mechanisms, thereby enhancing the mechanical performance compared with conventionally fabricated counterparts. Notably, the unique dislocation cell patterns, which are caused by residual stresses arising from the large temperature gradient and thermal cycling during L-AM, significantly contribute to the strength (He et al., 2022; Kwon et al., 2022). Sui et al. (2022) investigated L-AM-processed FeCoCrNiMo and reported that its hierarchical eutectic and irregular lamellar structures resulted in high hardness and wear resistance. Furthermore, in our previous work, we demonstrated the capability of L-AM for fabricating FeCoCrNiMo,  $ \chi = 0.3 $ and 0.5) HEAs with good mechanical properties (Lin et al., 2024, 2023). Deformation twinning and micro/nanoprecipitates such as  $ \sigma $ phases were observed when the Mo fraction exceeded 0.3.

In this study, we utilized laser powder bed fusion (L-PBF) additive manufacturing to fabricate a series of defect-free FeCoCrNiMo $ _x $ HEAs with varying Mo contents (x = 0, 0.1, 0.3, and 0.5). The mechanical properties and microstructural evolution were systematically investigated at room and elevated temperatures. The thermal stability and uniaxial tensile deformation behavior were studied by electron backscatter diffraction (EBSD) and transmission electron microscopy (TEM). Additionally, ab initio calculations and molecular

dynamics (MD) simulation models were established to quantify changes in the microscale lattice strain and stacking fault probability associated with plastic deformation. This work provides a quantitative assessment of the effects of the hierarchical microstructure on the mechanical response of L-PBF-processed FeCoCrNiMo $ _{x} $ HEAs, which is beneficial for enhancing their high-temperature performance as structural materials.

### 2. Materials and methods

### 2.1. Powder preparation and L-PBF process

To fabricate the FeCoCrNiMoₓ HEAs (x = 0, 0.1, 0.3, and 0.5; Mo content = 0, 2.44, 6.98, and 11.11 at%, respectively), denoted as MoO, Mo1, Mo3, and Mo5, respectively, equiatomic FeCoCrNi and FeCoCrNiMo powders with spherical particles (diameter: 15–53 μm) were produced by gas atomization. The powders were then mixed at different molar ratios in a three-dimensional mixer at 40 rpm for 5 h under a protective Ar atmosphere (Fig. 1a). Next, L-PBF was conducted using a RENISHAW AM-400 platform with a preheating temperature of 120 °C. The processing parameters were as follows: bidirectional scanning speed, 750 mm/s; laser power, 200 W; hatch spacing, 80 μm (MoO, Mo1, and Mo3) or 70 μm (Mo5); layer thickness, 40 μm; and rotation between layers, 67°. Blocks with

<div style="text-align: center;">a</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_148_465_972_943.jpg" alt="Image" width="75%" /></div>


<div style="text-align: center;">b</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_130_980_977_1303.jpg" alt="Image" width="77%" /></div>


<div style="text-align: center;">c</div>


<div style="text-align: center;">Fig. 1. L-PBF additive manufacturing procedures and prepared samples for tensile tests: (a) different Mo content ratios are achieved by adjusting the ratio of FeCoCrNi and FeCoCrNiMo powders, (b) Schematic diagram of L-PBF process, (c) Size of tensile specimen at room temperature (dogbone shape) and high temperature (600 °C, round rod shape).</div>


dimensions of  $ 80 \times 40 \times 20 $ mm were fabricated (Fig. 1b).

#### 2.2. Mechanical testing

Mechanical testing was conducted using dog-bone samples (room-temperature tests) or rod-shaped samples (high-temperature tests) (Fig. 1c). The samples were extracted from the center of the L-PBF-processed blocks via electrical discharge machining. Tensile tests were performed until failure using a 3910-type microcomputer-controlled electronic universal testing machine at a crosshead speed of 0.5 mm/min (initial strain rate:  $ \sim3 \times 10^{-4} \, s^{-1} $).

### 2.3. Microstructural characterization

The microstructural characteristics and fracture surfaces of the tensile samples were characterized using field-emission scanning electron microscopy (SEM; ZEISS-EVO 18) in backscattered electron mode and EBSD. Field-emission TEM (FEI-Tecnai G2 F30) and energy-dispersive X-ray spectroscopy (EDS) were used to analyze the microstructures and chemical compositions of the samples. The crystal structure and dislocation morphology of the matrix and secondary phases were characterized by TEM. The microstructural evolution of Mo5 was characterized by SEM, EBSD, EDS, and TEM.

#### 2.4. Ab initio calculations and molecular dynamics (MD) simulations

Ab initio calculations were conducted using density functional theory (DFT) (Hohenberg and Kohn, 1964), employing the exact muffin-tin orbitals method to solve the Kohn–Sham equations (Andersen et al., 1995; Vitos, 2001; Vitos et al., 2000). The Perdew–Burke–Ernzerhof exchange–correlation functional was used for self-consistent determination of the charge density and total energy (Perdew et al., 1996). Given that the magnetic ordering temperature of FeCoCrNi is well below room temperature, all spin-polarized DFT calculations were performed assuming a paramagnetic state (Gyorffy et al., 1985). The paramagnetic state was described using a disordered local moment approach. The coherent potential approximation was employed to model the chemical disorder (Gyorffy, 1972; Vitos et al., 2001).

For SFE calculations, we followed the methodology described by Schönecker et al. (Schönecker et al., 2021). The thermal lattice expansion and magnetic contributions were considered to account for the temperature dependence of the SFE. Specifically, we derived the lattice expansion of the FCC phase by minimizing the free energy  $ F(V, T) = E^{\mathrm{PM}}(V) - TS^{\mathrm{PM}}(V) + F^{\mathrm{vib}}(V, T) $ over the atomic volume  $ V $ for a given temperature  $ T $, where  $ E^{\mathrm{PM}} $ and  $ S^{\mathrm{PM}} $ are the total energy and magnetic entropy of the paramagnetic state, respectively, and  $ F^{\mathrm{vib}} $ is the vibrational free energy. Next, the FCC lattice parameter corresponding to a certain  $ T $ was employed to calculate the SFE.

<div style="text-align: center;"><img src="imgs/img_in_chart_box_112_792_457_1034.jpg" alt="Image" width="31%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_466_796_826_1033.jpg" alt="Image" width="33%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_113_1037_453_1284.jpg" alt="Image" width="31%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_459_1040_974_1282.jpg" alt="Image" width="47%" /></div>


<div style="text-align: center;">Fig. 2. Tensile properties of the L-PBF additively manufactured FeCoCrNiMox (x = 0, 0.1, 0.3, and 0.5) HEAs: (a) 25 °C, (b) 600 °C. “∞” denotes the UTS point of sample. (c) Evolution of the work hardening rate samples over the true strain at 600 °C, (d) Comparison of the ultimate tensile strength (UTS) and uniform elongation (UFE) at elevated temperature (600 °C) of the additively manufactured FeCoCrNiMox in this work and some reported alloys (References for these data are given in the Supplementary Materials).</div>


considering the contributions from  $ E^{\mathrm{PM}} $ and  $ S^{\mathrm{PM}} $.  $ F^{\mathrm{vib}} $ of the FCC phase was calculated using the Debye–Grüneisen model (Moruzzi et al., 1988).  $ S^{\mathrm{PM}} $ was calculated with consideration to the transverse degrees of freedom using the mean-field expression for uncorrelated magnetic moments (Grimvall, 1975).

The open-source MD simulation software, LAMMPS, is employed for the uniaxial stretching simulation (Plimpton, 1995). The potential function used is the modified embedded atom method (MEAM) potential for six elements (Ni-Cr-Co-Mo-V-Al) developed by Wang et al. (2023), and it is incorporated into the HEA model's machine learning through a neural network. Liu et al. (2024) and (Shi et al., 2024) respectively used this potential function to verify the deformation mechanisms of medium entropy alloy (MEA) and HEAs, achieving ideal results. The uniaxial tensile simulations of the single crystal nanowire are conducted at two temperatures: 25 °C and 600 °C. For visualization, the open-source software OVITO is used.

To obtain atomic models with random elements distribution, we first conducted energy minimization on the initial models, followed by relaxation for 20 ps at 25 °C. Using a combination of MC atom swaps and MD hybrid method, we constructed atomic models for alloy containing CSRO based on the initial models. After MC simulation, we annealed the model from 1227 °C to 25 °C and 600 °C at a 1 °C/ps rate. For a second lattice relaxation under canonical ensemble (NVT), we switched the model to non-periodic boundary conditions on the x, y, and z axes. The y-direction deformation is performed at an engineering strain rate of  $ 2 \times 10^8 $ s $ ^{-1} $. At the top and bottom regions of the simulation box, rigid blocks containing immobile atoms were positioned. A constant velocity was applied to these blocks in opposite directions to deform the model. Free boundary conditions were established on the planes parallel to the loading axis. During the tensile process, velocity rescaling was performed at every step. While this may influence the thermal conductivity analysis of HEAs, both the literature (Chen et al. 2021) and our research (Liu et al. 2024) indicate that this approach stabilizes the deformation temperature, with negligible impact on deformation twinning. We compared velocity rescaling every 1, 5, 10, and 100 steps, as well as a case with no rescaling. The lack of thermal energy in the system does not significantly affect the MD simulation results.

In the simulation process, the strain rate is actually  $ 10^8 - 10^9 \, \text{s}^{-1} $. (Chen et al., 2021; Liu et al., 2024) This calculation speed is closer to the experimental results in macroscopic experiments, although there is a large gap between the calculation speed and the actual speed. However, due to the effects of size effects, etc., it is possible to qualitatively analyze the deformation mechanism.

### 3. Results and discussion

### 3.1. Mechanical properties

Figs. 2a and 2b show the uniaxial tensile stress–strain curves of the as-built L-PBF-processed samples with varying Mo contents (Mo0, Mo1, Mo3, and Mo5) at temperatures of 25 and 600 °C. At room temperature, Mo enhances both the strength and ductility (Table 1). Compared with Mo0, the yield strength (YS) of Mo1 increases from 566 to 609 MPa and the ductility increases from 19% to 27%. Mo3 and Mo5 exhibit even higher room-temperature mechanical properties.

The mechanical performance of all samples decreases significantly at elevated temperatures, with their YS and ultimate tensile strength (UTS) varying considerably. The ductility of Mo0 is less than 10%, indicating its unsuitability for high-temperature applications. Mo1 displays dynamic strain strengthening during high-temperature tensile loading; however, its ductility is still less than 10%. A notable disparity is observed in the high-temperature tensile performance of Mo3 and Mo5. For Mo3, the YS, UTS, and uniform elongation at 600 °C are 20%, 57%, and 1513% higher, respectively, than those of Mo0. The strain hardening of Mo3 is essentially the same as that at room temperature (Fig. 2c). Consequently, it demonstrates a successful balance between strength and ductility at high temperatures. By contrast, the ductility of Mo5 approaches the lower limit of the accentable range (10%).

At 600 °C, Mo1 exhibited significant serrated flow behavior, whereas Mo0, Mo3, and Mo5 did not show this phenomenon at this temperature. It can be seen that at the same temperature, serrated flow behavior is closely related to the Mo content. The essence of serrated flow is the pinning effect of solute atom clusters on dislocations, which increases the flow stress. When the flow stress increases to a certain value, the dislocations break through the solute clusters, causing a sudden drop in flow stress. These two actions alternate, forming the serrated flow behavior. In Mo0, no Mo element was added, and the structure contains only Fe, Co, Cr, and Ni elements, with atomic radii of 124.1, 125.3, 124.9, and 124.6 Å, respectively. Since the atomic diameters are relatively close, the lattice distortion effect is not significant, and the pinning effect of solute atoms on dislocation motion is low. Thus, no serrated flow behavior occurs. In Mo1, Mo atoms (with a diameter of 136.3 Å) aggregate into solute clusters near dislocations, significantly increasing the

<div style="text-align: center;">Summary of mechanical properties of the L-PBF additively manufactured FeCoCrNiMox (x = 0, 0.1, 0.3, and 0.5) HEAs at different temperature conditions.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Sample</td><td style='text-align: center; word-wrap: break-word;'>Temperature,  $ \degree $C</td><td style='text-align: center; word-wrap: break-word;'>YS, MPa</td><td style='text-align: center; word-wrap: break-word;'>UTS, MPa</td><td style='text-align: center; word-wrap: break-word;'>UFE, %</td><td style='text-align: center; word-wrap: break-word;'>TE, %</td></tr><tr><td rowspan="2">Mo0</td><td style='text-align: center; word-wrap: break-word;'>25</td><td style='text-align: center; word-wrap: break-word;'>566</td><td style='text-align: center; word-wrap: break-word;'>719</td><td style='text-align: center; word-wrap: break-word;'>18.15</td><td style='text-align: center; word-wrap: break-word;'>19.82</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>600</td><td style='text-align: center; word-wrap: break-word;'>398</td><td style='text-align: center; word-wrap: break-word;'>420</td><td style='text-align: center; word-wrap: break-word;'>1.20</td><td style='text-align: center; word-wrap: break-word;'>1.25</td></tr><tr><td rowspan="2">Mo1</td><td style='text-align: center; word-wrap: break-word;'>25</td><td style='text-align: center; word-wrap: break-word;'>609</td><td style='text-align: center; word-wrap: break-word;'>776</td><td style='text-align: center; word-wrap: break-word;'>27.46</td><td style='text-align: center; word-wrap: break-word;'>36.51</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>600</td><td style='text-align: center; word-wrap: break-word;'>407</td><td style='text-align: center; word-wrap: break-word;'>473</td><td style='text-align: center; word-wrap: break-word;'>6.71</td><td style='text-align: center; word-wrap: break-word;'>8.23</td></tr><tr><td rowspan="2">Mo3</td><td style='text-align: center; word-wrap: break-word;'>25</td><td style='text-align: center; word-wrap: break-word;'>698</td><td style='text-align: center; word-wrap: break-word;'>953</td><td style='text-align: center; word-wrap: break-word;'>25.02</td><td style='text-align: center; word-wrap: break-word;'>27.78</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>600</td><td style='text-align: center; word-wrap: break-word;'>477</td><td style='text-align: center; word-wrap: break-word;'>661</td><td style='text-align: center; word-wrap: break-word;'>19.35</td><td style='text-align: center; word-wrap: break-word;'>22.98</td></tr><tr><td rowspan="2">Mo5</td><td style='text-align: center; word-wrap: break-word;'>25</td><td style='text-align: center; word-wrap: break-word;'>830</td><td style='text-align: center; word-wrap: break-word;'>1091</td><td style='text-align: center; word-wrap: break-word;'>19.38</td><td style='text-align: center; word-wrap: break-word;'>19.93</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>600</td><td style='text-align: center; word-wrap: break-word;'>578</td><td style='text-align: center; word-wrap: break-word;'>799</td><td style='text-align: center; word-wrap: break-word;'>11.16</td><td style='text-align: center; word-wrap: break-word;'>11.33</td></tr></table>

resistance to dislocation motion, leading to the formation of serrated flow behavior. As the Mo content further increases, the sluggish diffusion effect of HEAs gradually suppresses the diffusion behavior of solute atoms, reducing the tendency to form solute atom clusters around dislocations, thereby eliminating serrated flow behavior.

From the perspective of material plasticity, the plasticity of Mo1 at 600 °C is much higher than that of Mo0. Our previous research (Lin et al., 2022) has revealed that the high-temperature brittleness of Mo0 is caused by the nanocluster formation of elements at the grain boundaries. Therefore, the addition of Mo in Mo1 and Mo3 improves the bonding strength at the grain boundaries, enhancing high-temperature plasticity. The slight decrease in plasticity of Mo5 compared to Mo3 is due to the embrittlement caused by the growth of the σ phase.

Fig. 2d compares the high-temperature (>600 °C) mechanical properties of various FeCoCrNi-based HEAs, Ti-based alloys, and Ni-based superalloys. Mo3 and Mo5 exhibit comparatively remarkable mechanical performance, particularly regarding the strength–ductility trade-off. This advancement demonstrates the potential of these alloys for use in high-temperature environments.

### 3.2. Initial microstructures of L-PBF-processed FeCoCrNiMo $ _{x} $ HEAs

For a more comprehensive understanding of the reasons behind the changes in performance, we conducted a detailed microstructural analysis. Fig. 3 presents SEM images of the additively manufactured FeCoCrNiMoₓ HEAs. The samples are nearly defect-free, although a few small round pores (<1 μm) are visible near the fusion lines. Moreover, a distinct dendritic structure is concentrated at the overlaps of the melt pools, with clear dendrite and interdendrite regions (Figs. 3a, 3b, and 3c, insets). In comparison with MoO (Fig. 3a), the Mo-containing samples exhibit sharper dendrites (Figs. 3b and 3c). Because of the significant temperature gradient and thermal cycling during L-PBF, the initial solidification occurs faster at the top of the molten pool than at the bottom (Hu et al., 2022; Munusamy and Jerald, 2023; Wang et al., 2023b). This results in dendritic growth at the top of the pool, whereas the bottom maintains planar crystal growth. Small grains form in the intersecting areas of the melt pools (Fig. 3d, inset). Therefore, the additively manufactured FeCoCrNiMoₓ HEAs exhibit microstructural heterogeneity, with a grain size distribution of a few microns to tens of microns.

Fig. 4 presents the EBSD results of the as-built FeCoCrNiMoₓ HEAs. From the inverse pole figure maps, the MoO grains show a clear tendency to grow along the direction of construction (z direction). This is attributed to the thermal gradient and optimal solidification orientation (Körner et al., 2020). Thus, the grains have a unidirectional epitaxial columnar shape. In addition, the matrix exhibits a relatively obvious 100<111> texture, as illustrated in the pole figure in Fig. 4a3. However, the introduction of Mo induces notable changes (Figs. 4b1, 4c1, and 4d1), with a more random grain orientation. Furthermore, the average grain size increases from 35.1 μm for MoO to 57.5 μm for Mo3. Given that Mo is a refractory element, a higher energy density is required for preparation. Therefore, the

<div style="text-align: center;">a</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_115_743_540_1028.jpg" alt="Image" width="39%" /></div>


<div style="text-align: center;">b</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_549_742_973_1028.jpg" alt="Image" width="38%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_117_1037_542_1320.jpg" alt="Image" width="39%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_549_1037_972_1320.jpg" alt="Image" width="38%" /></div>


<div style="text-align: center;">Fig. 3. Typical microstructure of L-PBF additively manufactured FeCoCrNiMox samples: (a) Mo0, (b) Mo1, (c) Mo3, and (d) Mo5. Distinct dendritic structure is concentrated at the overlap of the molten pool. Small grains generate in the intersection area of the molten pool.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_114_109_326_293.jpg" alt="Image" width="19%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_330_109_541_294.jpg" alt="Image" width="19%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_545_109_755_294.jpg" alt="Image" width="19%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_761_108_974_294.jpg" alt="Image" width="19%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_114_301_325_459.jpg" alt="Image" width="19%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_329_301_541_461.jpg" alt="Image" width="19%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_543_300_754_460.jpg" alt="Image" width="19%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_112_463_324_677.jpg" alt="Image" width="19%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_327_467_549_671.jpg" alt="Image" width="20%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_547_469_758_670.jpg" alt="Image" width="19%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_761_302_972_669.jpg" alt="Image" width="19%" /></div>


<div style="text-align: center;">Fig. 4. Typical microstructure of L-PBFed samples: (a1-a3) Mo0, (b1-b3) Mo1, (c1-c3) Mo3, and (d1-d3) Mo5. (a1, b1, c1, d1) EBSD inverse pole figure (IPF) maps showing the grain size and morphology. (a2, b2, c2, d2) KAM images superimposed with high angle grain boundaries (HAGBs, black lines). (a3) Texture orientation of Mo showing 100<111>; (b3, c3) Statistics for the grain size; (d3) Distribution of grain state in recrystallized, substructured, and deformed.</div>


<div style="text-align: center;">Summary of microstructural characteristics of the as-built FeCoCrNiMox HEAs  $ (x = 0, 0.1, 0.3, \text{ and } 0.5) $.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Sample</td><td style='text-align: center; word-wrap: break-word;'>Mo at%</td><td style='text-align: center; word-wrap: break-word;'>Avg. grain size,  $ \mu $m</td><td style='text-align: center; word-wrap: break-word;'>GND density,  $ \times 10^{14} $ /m $ ^{2} $</td><td style='text-align: center; word-wrap: break-word;'>Fraction of RX, %</td><td style='text-align: center; word-wrap: break-word;'>Texture orientation</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Mo0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>35.1</td><td style='text-align: center; word-wrap: break-word;'>8.45</td><td style='text-align: center; word-wrap: break-word;'>2.9</td><td style='text-align: center; word-wrap: break-word;'>100&lt;111&gt;</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Mo1</td><td style='text-align: center; word-wrap: break-word;'>2.44</td><td style='text-align: center; word-wrap: break-word;'>47.4</td><td style='text-align: center; word-wrap: break-word;'>9.84</td><td style='text-align: center; word-wrap: break-word;'>13.3</td><td style='text-align: center; word-wrap: break-word;'>100&lt;111&gt;</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Mo3</td><td style='text-align: center; word-wrap: break-word;'>6.98</td><td style='text-align: center; word-wrap: break-word;'>57.5</td><td style='text-align: center; word-wrap: break-word;'>8.25</td><td style='text-align: center; word-wrap: break-word;'>10.7</td><td style='text-align: center; word-wrap: break-word;'>100&lt;111&gt;</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Mo5</td><td style='text-align: center; word-wrap: break-word;'>11.11</td><td style='text-align: center; word-wrap: break-word;'>51.9</td><td style='text-align: center; word-wrap: break-word;'>8.99</td><td style='text-align: center; word-wrap: break-word;'>6.4</td><td style='text-align: center; word-wrap: break-word;'>100&lt;111&gt;</td></tr></table>

average geometrically necessary dislocation density of Mo3, as calculated from the kernel average misorientation, is similar to that of Mo0. The microstructural characteristics are summarized in Table 2.

The variations in the grains (orientation, recrystallization, and size) of the FeCoCrNiMoₓ HEAs highlight the complex interplay between the composition and processing parameters, resulting in differences in the mechanical properties. Overall, the multiscale heterogeneity is derived from microscale lattice defects (Zhang et al., 2018), requiring more geometrically necessary dislocations to achieve microstructural deformation during L-PBF. As shown in Fig. 4d₃, Mo₅ contains a few recrystallized grains, whereas most grains are substructured and deformed, indicating a high dislocation density. In addition to the high density of dislocation cells caused by thermal residual stress, slow elemental diffusion within HEAs is also considered to hinder recrystallization (Miracle and Senkov, 2017). The fraction of partially recrystallized grains is affected by the Mo concentration (Ming et al., 2019), as well as laser-induced structural deformation (Peng et al., 2024) and precipitation (He et al., 2021a). The recrystallized fraction of the FeCoCrNiMoₓ samples varies from 2.9% to 13.3%, which will affect the dislocation hardening behavior during tensile deformation.

Fig. 5 shows the dislocation morphology and elemental segregation of the FeCoCrNiMoₓ HEAs, as characterized by TEM and EDS. Laser-printed samples typically exhibit hexagonal dislocation cell patterns because of residual stresses during solidification (He et al., 2022). However, the dislocation cell patterns are not obvious in Mo0. As the Mo content increases, the dislocation cell features become more obvious and the cell walls become sharper. The cell wall thickness decreases from approximately 200 nm for Mo1 to 50 nm for Mo5, and the cell size increases slightly. Some stacking faults can also be observed in Mo5.

Mo3 and Mo5 contain rod-shaped nanoscale σ-phase precipitates at the grain boundaries (Figs. 5c and 5d). This is because Mo, a refractory metal with a large atomic radius, is likely to be enriched at locations with large lattice distortions, such as grain boundaries,

<div style="text-align: center;">L-PBF additive manufacturing as-built state</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_112_143_977_601.jpg" alt="Image" width="79%" /></div>


<div style="text-align: center;">Fig. 5. TEM image reveals the microstructure of the dislocation networks of the as-built FeCoCrNiMox HEAs: (a) Mo0, (b) Mo1, (c) Mo3, and (d) Mo5; EDS mapping results of the Cr-rich nano precipitates in rod shape (σ phase) and blocky shape (μ phase) in Mo3 and Mo5 samples. Nano-twins generate in Mo5 samples inside of the DCP. The white arrows highlight the emission of stacking faults (SFs) with the DCP.</div>


which act as nucleation sites. Segregated Cr/Mo solutes can also redistribute or diffuse into mobile grain boundaries during matrix growth (He et al., 2021a), thereby promoting σ-phase nucleation along the grain boundaries. The diffusion rate of Mo is much slower than that of Cr. In addition, it is present in relatively lower concentrations than the other elements in the HEA. Therefore, it is primarily Cr (He et al., 2021a) that partitions into the σ phase. In addition to the nanoscale σ-phase precipitates, blocky μ-phase precipitates can also be observed (Cr-rich Mo). The μ-phase precipitates appear at the edges of the σ-phase precipitates, indicating that they may be generated by transformation of the σ phase during solidification. Sui et al. (Sui et al., 2022) credited μ-phase formation to the lattice strain produced by excessive Mo, which makes the σ phase unable to maintain its tetragonal structure. The release of lattice strain

<div style="text-align: center;">Post-necking state after tensile deformation @25°C</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_113_926_975_1303.jpg" alt="Image" width="79%" /></div>


<div style="text-align: center;">Fig. 6. Deformation microstructures evolution of L-PBFed FeCoCrNiMox sample at the post-necking deformation stage under tensile tests at room temperature is presented. Bright-field and dark-field TEM images reveal the different twinning effects of the FeCoCrNiMox HEAs: (a) Mo0, (b) Mo1, (c) Mo3, and (d) Mo5.</div>


causes the σ phase to transform into the rhombohedral μ phase. Furthermore, supersaturated Mo induces σ-phase formation along the grain boundaries, which effectively inhibits the formation of Mo-containing alloy through the pinning effect and can effectively delay recrystallization and grain growth (Linder et al., 2024; Miracle and Senkov, 2017).

### 3.3. Microstructural evolution of FeCoCrNiMo $ _{x} $ HEAs during deformation at 25 and 600 °C

Fig. 6 shows TEM images of near-neck regions of the samples deformed at room temperature. These images demonstrate the distinctive role of twinning in the room-temperature plastic deformation of FeCoCrNiMo_x HEAs. However, there is a notable variation in the density and width of twins across different samples. Specifically, the presence of twins in the MoO, Mo1, and Mo3 samples is more pronounced compared to the Mo5 sample, where the number is relatively small, as shown in Fig. 6d2. This suggests that the critical stress required for twin activation in the as-built Mo5 sample is significantly higher than the other samples, even though it exhibits greater strength and ductility than the Mo0 and Mo1 HEAs. This is primarily due to the presence of a significant amount of σ precipitates (Fig. 5) in Mo5. These precipitates can partially hinder the movement of dislocations, thereby preventing the formation of stacking faults in the matrix (Cai et al., 2017). Consequently, this reduces the likelihood of stacking faults, and further decreases the probability of twin formation. Additionally, the significant plastic deformation during the stretching process in Mo3, combined with the lower quantity of σ precipitates, leads to a much higher number of twins in Mo3 compared to Mo5.

According to Table 1, the strength of MoO and Mo1 decreased by 40% at high temperatures, while the ductility of Mo3 and Mo5 only decreased by 30%. Moreover, Mo3 and Mo5 retained a higher percentage of elongation. To understand this difference, we conducted high-temperature fracture surface TEM analysis. Fig. 7 displays the TEM characterization results of the near-necking position of samples with different Mo contents after deformation at high temperatures. We observed that due to the lack of precipitates hindering their movement, the grains in the MoO and Mo1 samples were significantly elongated post-deformation. These lamellar grain boundaries act as strengthening barriers, accumulating intragranular dislocations and consequently reducing the ductility of the samples. In the Mo3 and Mo5 sample, some cellular dislocations remained visible, and short rod-shaped precipitates of the σ phase were located on the dislocation cell wall. These precipitates played a pinning role in the movement of the dislocation cell, contributing to its high-temperature stability. It is worth noting that in the Mo3 and Mo5 samples, the hindrance of dislocation motion by precipitates results in the accumulation of a large number of dislocations at grain boundaries. This leads to stress concentrations exceeding the critical twinning stress level, causing the formation of deformation twins. This indicates that in addition to the dislocation coordination deformation observed in MoO and Mo1, twinning induced plasticity (TWIP) effects also came into play. Since the deformation temperature does not reach the secondary precipitation temperature of the σ phase, the ratio of precipitates will not increase further during the high-temperature deformation process (Elmer et al., 2007). High-density dislocations pile up along the hard σ-phase precipitates, hindering further dislocation slip. The excessive σ-phase cannot deform coherently with the matrix, leading to cracking under low plastic deformation conditions. As a result, stress concentration-induced cracking occurs earlier in Mo5 than in Mo3 sample during tensile deformation.

<div style="text-align: center;">Post-necking state after tensile deformation @600°C</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_114_946_974_1321.jpg" alt="Image" width="78%" /></div>


<div style="text-align: center;">Fig. 7. Deformation microstructures evolution of L-PBFed FeCoCrNiMox sample at necking-fracture state after tensile deformed at 600 °C: (a) Mo0, (b) Mo1, (c) Mo3, and (d) Mo5. GB: grain boundary.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_111_110_973_486.jpg" alt="Image" width="79%" /></div>


<div style="text-align: center;">Fig. 8. Necking-fracture morphology of (a) Mo3 and (b) Mo5 samples after tensile deformation at 25 °C.</div>


### 3.4. Fracture morphology of Mo3 and Mo5 at 25 and 600 °C

To elucidate the fracture mechanisms of the Mo3 and Mo5 samples, we conducted an analysis of the fracture surfaces of the tensile specimens at 25 °C and 600 °C. Fig. 8 illustrates the room-temperature fracture morphologies of Mo3 and Mo5. The fracture surfaces are characteristic of FCC materials, with high densities of tears and dimples. Under uniaxial loading, the initial crack extends in the tensile direction, forming voids during the crack extension stage. The connections between these voids result in fractures. Some tongue-shaped pits or protrusions formed by extension of the cleavage cracks along the twin boundaries are visible (Fig. 8b2). This phenomenon is consistent with the findings of Sui et al. (Sui et al., 2022). Fig. 8a3 indicates that the molten pool boundary is susceptible to fracture.

Fig. 9 illustrates the high-temperature fracture morphologies of Mo3 and Mo5. The fracture surface of Mo3 still exhibits ductile fracture characteristics, albeit with a diminished presence of dimples as compared to that at room temperature. The emergence of twins during the latter stages of deformation renders the fracture surface akin to the room-temperature fracture surface of Mo5, with tongue-shaped cleavage crack patterns. By contrast, the high-temperature fracture surface of Mo5 exhibits quasi-cleavage traits. Cleavage steps are formed by fracture along the crystal planes at varying heights. The fracture surface of Mo5 (Fig. 9b2) is considerably flatter than that of Mo3 (Fig. 9a2), suggesting that the fracture strain was relatively constrained during the tensile process. This observation aligns with the high-temperature tensile stress-strain curves. The presence of σ-phase precipitates, which are hard and brittle intermetallic compounds, enhances the compressive strength but concurrently reduces the fracture strain.

<div style="text-align: center;">a1</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_112_949_972_1322.jpg" alt="Image" width="78%" /></div>


<div style="text-align: center;">Fig. 9. Necking-fracture morphology of additively manufactured CoCrFeNiMox HEA samples after tensile deformation at 600 °C: (a) Mo3 and (b) Mo5.</div>


Comparing the room- and high-temperature tensile fracture morphologies of Mo3 and Mo5 reveals a trend of transition and transformation in the fracture characteristics, suggesting that the strength of additively manufactured FeCoCrNiMo $ _x $ HEAs can be significantly enhanced by adding an appropriate amount of Mo. Moreover, it potentially reveals the Mo content window for tuning the mechanical properties of FeCoCrNiMo $ _x $ HEAs.

<div style="text-align: center;"><img src="imgs/img_in_chart_box_195_275_888_699.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_195_717_893_1079.jpg" alt="Image" width="64%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_204_1098_891_1302.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Fig. 10. (a) The diagram of the nonequilibrium solidification thermodynamic process and phase evolution of Mo0, Mo1, Mo3 and Mo5 HEAs calculated using Thermo-calc software, specific elemental content in solid phase during solidification process of (b) Mo1 and (c) Mo5, (d) Comparison of printed microstructure characteristics with varying Mo additions.</div>


<div style="text-align: center;">a Closed-packed planes</div>


<div style="text-align: center;">b Perfect stacking Intrinsic stacking fault</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_107_230_940_681.jpg" alt="Image" width="76%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_122_705_937_1261.jpg" alt="Image" width="74%" /></div>


<div style="text-align: center;">Fig. 11. (a) Schematics of close-packed planes in the FCC structure with three possible atomic positions A, B, or C, selected crystallographic directions, partial Burgers vectors. (b) Schematic view of fault-free FCC lattice and FCC lattice with intrinsic stacking fault. A, B, and C, and associated color-coded spheres indicate the stacking sequence of atoms and the thin lines describe the undistorted and tilted nine-layers unit cells used for calculating the  $ \gamma_{isf} $. (c) Ab initio calculation for  $ \gamma_{isf} $ of the FeCoCrNiMox HEAs as a function of the Mo content and temperature. The solid lines indicate the results from 200 K to 1000 K for 0 at%, 6 at%, and 11 at% Mo-doped into FeCoCrNi matrix, respectively.</div>


#### 3.5. Solidified phase equilibrium state of FeCoCrNiMo $ _{x} $ HEAs

The σ-phase is brittle, and therefore, its presence is generally detrimental for long-term applications. However, in this study, the addition of Mo promoted the precipitation of the σ-phase at grain boundaries, which further hindered cell deformation at high temperatures. Additionally, the pinning effect suppressed grain boundary migration, enhancing the high-temperature strength and plasticity of the HEA. Therefore, it is necessary to study the precipitation behavior of the σ-phase. Fig. 10 presents the change in the phase and element ratios during the solidification of the melt pools for different samples. The melting point ( $ T_m $) of the HEAs decreases from 1446 °C for Mo0 to 1381 °C for Mo5 (Fig. 10a). The FCC matrix forms from the liquid phase during solidification, accompanied by σ-phase precipitation for the Mo-doped HEAs. The onset of FCC solidification and σ-phase precipitation occur at different solid-phase molar fractions, although the step distance (molar amount) is much shorter for Mo3 than for Mo1 and Mo5. In fact, σ-phase precipitation in Mo3 begins almost simultaneously with the solidification of the FCC matrix.

Mo1 and Mo5 exhibit a similar trend in terms of the solid-phase content (Figs. 10b and 10c), which is quite different from that of Mo3 (Lin et al., 2023). In Mo3, the Mo-rich σ phase precipitates first, followed by simultaneous precipitation of the FCC and σ phases. By contrast, in Mo1 and Mo5, the Mo-rich φ phase precipitates later in the solidification process. As summarized in Fig. 10d, nanosized σ and μ phases precipitate in the subgrains and at the subgrain boundaries owing to the two-stage solidification (Lin et al., 2023). The differences in the fractions and distributions of precipitate phases caused by the different Mo contents and the coupling effect with dislocations lead to different degrees of sharpening of the dislocation cell walls (Fig. 5). It is worth noting that dynamic recrystallization may occur at the high-temperature tensile conditions of 600 °C (>0.35T_m). However, the Mo-rich precipitates that form during L-PBF could suppress grain boundary migration via pinning, thereby increasing the size of the recrystallized grains (Wang et al., 2017).

#### 3.6. Ab initio calculations and molecular dynamics (MD) simulations for revealing the effects of Mo content and temperature

According to Figs. 2, 6, and 7, there are significant differences in the plasticity of HEAs with varying Mo content. To thoroughly investigate the reasons behind these differences, we conducted ab initio calculations for auxiliary analysis. As an important strengthening and hardening mechanism, the morphology and distribution of the deformation twins are closely related to the Mo content and temperature, which directly affect the SFE (Chang et al., 2021; Wang et al., 2017). The intrinsic SFE  $ \gamma_{isf} $, representing the energy barrier of generating intrinsic SFs, determines twin formation. In FCC crystals, we consider the usual $ _{FCC}/2 $ [10T](111)FCC slip system where a perfect lattice dislocation can dissociate into two Shockley partials with Burgers vectors  $ b_{p1}^{FCC}=a_{FCC}/6[11\overline{2}]_{FCC} $ and  $ b_{p2}^{FCC}=a_{FCC}/6[2\overline{11}]_{FCC} $.  $ a_{FCC} $ is the FCC lattice parameter. The stacking sequence of (111)FCC close-packed planes is ABC[ABC] ABC..., where the labels A through C correspond to the three possible atomic positions in a (111)FCC plane. The schematic diagram is shown in Fig. 11a. Next, and intrinsic stacking fault, of energy  $ \gamma_{isFe} $ was created by shifting the top ten layers along the [1 1 2] direction by the Burgers vector of the Shockley partial  $ b_{p1}^{FCC} $, this resulted in a stacking sequence: ABC[BC]ABC, shown in Fig. 11b. Our ab initio calculation results, depicted in Fig. 11, reveal that  $ \gamma_{isF} $ is approximately -21, -33, and -48 mJ/m $ ^2 $ for HEAs with 0, 6, and 11 at% Mo, respectively, at room temperature. However, at 600 °C,  $ \gamma_{isF} $ is estimated to be approximately -9, -15, and -26 mJ/m $ ^2 $, respectively. Thus, the addition of Mo reduces  $ \gamma_{isF} $ for the as-built FeCoCrNiMo $ _{x} $ HEAs, especially at elevated temperatures. As the SFE increases, the dynamic recovery becomes more active at high temperatures, facilitating dislocation movement such as cross-slip. However, dynamic recovery occurs earlier during deformation at 600 °C than at 25 °C, leading to a rapid decrease in the work-hardening rate at high strain stages. For Mo5 (11 at%)), although it has a lower stacking fault energy, we did not observe a significant amount of twinning in the matrix. This is because dislocation slip and diffusion mechanisms are more active at high temperatures, which increases the activation stress for twinning deformation. Additionally, the presence of a large amount of  $ \sigma $-phase attached to the grain boundaries leads to fracture at lower strain values. This reduction in plastic deformation also decreases the occurrence of twinning to some extent. The dynamic Hall-Petch effect, induced by the twin boundary in Mo3, introduces new interfaces and reduces the dislocation mean free path, providing further contribution. Consequently, the dislocation cell patterns of the FeCoCrNiMo $ _{x} $ HEAs are altered by the

<div style="text-align: center;"><img src="imgs/img_in_chart_box_215_1056_495_1322.jpg" alt="Image" width="25%" /></div>


<div style="text-align: center;">b</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_529_1065_868_1322.jpg" alt="Image" width="31%" /></div>


<div style="text-align: center;">Fig. 12. (a) Schematic illustration of the uniaxial tensile MD simulation conducted on a single crystal Mo3 nanowire. (b) Simulated stress-strain curves at 25 °C and 600 °C show difference in elastic modulus and stress softening due to elevated temperature.</div>


temperature and Mo content, which is consistent with the experimental observations and TEM characterizations. Because the SFE evolution is critical for revealing the potential deformation mechanism in the activation of twinning, ab initio calculations provide valuable insight into the design of FeCoCrNiMoₓ HEAs.

In order to further explore the plastic deformation essence of Mo3 alloy, we conducted molecular dynamics simulations. In the MD simulations, the Mo3 tensile specimen was simulated using a single-crystal nanowire, as displayed in Fig. 12a. The model had an FCC crystal structure with a lattice constant of 3.60 Å. The crystallographic directions along the x, y, and z axes were [001], [110], and [110], respectively. The nanowire comprised 100,000 atoms, including 23,254, 23,259, 23,255, 23,256, and 6976 Fe, Co, Cr, Ni, and Mo atoms, respectively, thereby satisfying the atomic ratio of FeCoCrNiMo0.3 (Mo3). Periodic boundary conditions were applied in all three directions. The top and bottom layers, each measuring 27 Å along the y axis, were fixed. To simulate uniaxial tensile deformation, these fixed layers were extended in opposite directions along the y axis, with a stretching speed of 0.02 Å/ps. The deformation zone, subjected to stretching, measured 200 × 72 × 64 Å.

As illustrated in Fig. 12b, Mo3 shows significant stress softening at 600 °C compared to that at 25 °C. Moreover, the elastic modulus at 600 °C is significantly lower than that at 25 °C. As deformation proceeds, twinning occurs, which causes stress drops.

Figs. 13a and 13b illustrate the MD simulations of twin evolution in Mo3 during tensile deformation at room and high temperatures, respectively. The presence of Mo enhances the lattice distortion. During tensile deformation, stacking faults are generated. As the strain increases, these stacking faults accumulate, leading to the formation of micro twins (Tian et al., 2024). Despite the generation of micro twins at 25 °C, the growth of these micro twins is suppressed as the strain continues to increase, because a significant number of stacking faults accumulate. This results in an alternating structure of micro twins and stacking faults, thereby enhancing the ductility (Guo et al., 2024; He et al., 2021b; Jo et al., 2014).

As the temperature rises to 600 °C, the SFE gradually increases, as demonstrated by the ab initio calculation results in Fig. 11b. The local stress of twinning tends to increase with increasing temperature. Thus, the twin lamellae are larger than those at 25 °C, as displayed in Fig. 13b. The stacking faults expand during tensile straining, thereby consuming the twins. Consequently, the strength is reduced owing to the interaction between stacking faults and twins. Owing to the mutual interaction between the twins and stacking faults during tensile deformation, Mo3 still has good ductility at 600 °C.

Our calculations at the atomic scale indicate that when HEA yields, the ISF structure emerges within the crystal. Some researchers have characterized through TEM that stacking faults and slip are the initial structures observed during the yielding of FCC alloys. With increasing temperature,  $ \gamma_{isf} $ increases, but studies suggest that  $ \gamma_{ui} $ exhibits only slight variations. Temperature provides kinetic energy to atomic motion, leading to lower yield strength of materials at elevated temperatures. Tadmor and Bernstein introduced an alternative approach known as  $ \tau_{a} $ (Bernstein and Tadmor, 2004). The following expression can approximate this method (Wu et al., 2014).

 $$ \tau_{\mathrm{a}}=\left[1.136-0.151\frac{\gamma_{\mathrm{isf}}}{\gamma_{\mathrm{ui}}}\right]\sqrt{\frac{\gamma_{\mathrm{ui}}}{\gamma_{\mathrm{esf}}}} $$ 

Where the  $ \gamma_{ui} $ is the maximum value of intrinsic stacking faults, the  $ \gamma_{esf} $ is the minimum extrinsic stacking fault. The higher the value of  $ \tau_{a} $, the more likely it is to produce extrinsic stacking fault (ESF). As the temperature increases, the proportion of ISF transforming into ESF decreases gradually. ISF without transformation to ESF may generate two neighboring ISFs that can be understood as a twin (TW) structure. The transformation path of ISF into ESF and then into TW is the sole path of transformation for TW during the simulation. The transformation of ISF into TW requires a significant shear stress to take place, and the magnitude of the shear force,  $ \tau_{TW} $, can be determined using the following equation (Huang et al., 2006):

 $$ \tau_{\mathrm{TW}}=\frac{\gamma}{\mathrm{nb}_{1}}+\frac{\mathrm{Gb}_{1}\sqrt{\rho}}{\mathrm{n}} $$ 

A stress concentration factor, represented by n, is required in the early stages of nucleation, typically ranging from 2 to 4. The parameter  $ \gamma $ denotes the surface energy of the meta material, whereas b1 refers to the modulus of the Burgers vector of the Shockley partial dislocation and G represents the shear modulus.

According to the Taylor dislocation hardening model, the local shear stress,  $ \tau $TW, increases with an increase in dislocation density for FCC metals, which are known for their high-strain hardening ability(Huang et al., 2006).

<div style="text-align: center;"><img src="imgs/img_in_chart_box_326_1118_760_1304.jpg" alt="Image" width="39%" /></div>


<div style="text-align: center;">Fig. 13. Uniaxial tensile MD simulation results of Mo3 HEA. (a) A large number of stacking faults accumulate to form an alternating structure of micro twins and stacking faults at 25 °C. (b) The reduced stacking faults play interaction with micro twins, resulting in a decrease in strength at 600 °C.</div>


 $$ \tau_{\mathrm{TW}}=\alpha_{1}\mathrm{Gb}\sqrt{\rho}=\frac{\Delta\sigma}{\mathrm{M}} $$ 

Δσ represents the increase in tensile stress, the Taylor factor is denoted as M, α is a constant value, b represents the magnitude of the Burgers vector, and ρ is the dislocation density. The true tensile stress and resolved shear stress (Laplanche et al., 2016) at which twinning occurs are 550–600 MPa and 230–245 MPa, respectively. We illustrate the process of twin formation and the necessary range of true stress to induce twinning. At room temperature, all alloys exhibit high levels of yield stress, leading to twinning in each case. However, at 600 °C, Mo0 and Mo1 alloys display lower yield stress levels, while Mo3 and Mo5 exhibit higher levels, consequently resulting in twinning in the Mo3 and Mo5 alloys.

#### 3.7. Effect of hierarchical microstructure on mechanical properties

The multiscale strengthening mechanisms of the as-built FeCoCrNiMoₓ HEAs are important for clarifying the deformation mechanism, particularly the complex mechanical response of the hierarchical microstructure. For metals, the flow stress (σflow) can be expressed as

 $$ \sigma_{flow}=\frac{\sigma_{0}+\sigma_{\rho}+\sigma_{TW}+\sigma_{Intra}}{\sigma_{th}}+\frac{\sigma_{ss}+\sigma_{GB}+\sigma_{ppt}}{\sigma_{ath}} $$ 

where  $ \sigma_{ath} $ and  $ \sigma_{th} $ are thermally independent and dependent stress items, respectively, and  $ \sigma_{0} $ is the friction stress from lattice resistance (i.e., the Peierls–Nabarro stress), which is 125 MPa for Mo0 (Otto et al., 2013) and 237.19 MPa for Mo1 (Dai et al., 2021) at 25 °C.  $ \sigma_{0} $ can be calculated using the following formula (Ramakrishnan, 1996):

 $$ \sigma_{0}=\frac{2MG}{1-\nu}\exp\left(-\frac{2\pi c}{b(1-\nu)}\right) $$ 

where c is the distance between adjacent slip surfaces (0.206 nm; a/√3), M is the Taylor factor (~3.06 for the FCC matrix), α is a geometric factor (0.2 for FCC materials), b is the Burgers vector (0.146 nm for Shockley partial dislocations) (Dai et al., 2021), ν is Poisson's ratio, and G is the shear modulus, which is affected by the Mo content (Liu et al., 2020) and temperature (Huang et al., 2015). Here, G was calculated and measured experimentally using Young's modulus. Note that σ₀ is temperature-sensitive because it depends largely on the short-range atomic order and strength of the atomic bonds. As the temperature increases, the atomic vibrations increase, and the atomic bond strength decreases; therefore, σ₀ decreases (Wang et al., 2017).

From the ab initio calculations, the SFE of FeCoCrNiMoₓ HEAs decreases with increasing Mo content. Moreover, the stress is below the twinning threshold at the initial stage of yielding. Therefore, σᴬᴬ can be temporarily ignored at the yield deformation stage.

The coarse- and fine-grained regions and dislocation cell patterns inside the L-PBF-processed grains regulate dislocation slip during deformation (Liu et al., 2024). Thus, dislocation strengthening and back-stress strengthening in the initial deformation stage are very important and collectively increase the hetero-deformation-induced strengthening effect (Chu et al., 2024; Gao et al., 2023; Karthik and Kim, 2021). For the back stress, which comprises inter- and intragranular stresses, the intergranular stress is nearly zero at the initial stage of deformation (An et al., 2023), whereas the intragranular stress, caused by the heterogeneously distributed dislocations piling up at the interface (Gao et al., 2022) (i.e., high-density dislocation walls within the cellular structure in MoO), can be roughly estimated by the dislocation hardening model. For Mo1, Mo3, and Mo5, precipitation and solid-solution strengthening suppress intragranular stress generation. The empirical relationship for the dislocation hardening stress ( $ \sigma_{p} $) can be expressed as

 $$ \sigma_{\rho}=M\alpha Gb\sqrt{\rho_{GND}} $$ 

The geometrical factor  $ \alpha $ is also taken as a constant for FCC martial as 0.2 (Yim et al., 2019). The  $ \rho_{GND} $ can be obtained according to Table 2. Because dislocation and precipitation strengthening are both related to the cellular structure, the root mean square of the two effects, i.e.,  $ \sigma_{cc} = \sqrt{\sigma_{\rho}^{2} + \sigma_{ppt}^{2}} $, can be used to evaluate dislocation-cell strengthening in Mo-containing samples (Liu et al., 2023).

For the samples with Mo, the precipitation strengthening stress ( $ \sigma_{ppt} $) is expressed as

 $$ \sigma_{p p t}=\frac{G b}{2\pi}\frac{1}{D_{e}^{p p t}}\mathrm{I n}\left(\frac{D_{e}^{p p t}}{b}\right) $$ 

where  $ D_e^{ppt} $ denotes the average particle spacing, calculated using  $ d_p\left(\sqrt{\frac{\pi}{6f}} - \sqrt{\frac{2}{3}}\right) $. Here,  $ d_p $  $ d_p $ is the average radius of the precipitated particles and  $ f $ is the fraction of particles. The characteristics of the precipitates in Mo1, Mo3, and Mo5 were obtained by TEM and in our previous work (Lin et al., 2024, 2023). Note that  $ \sigma_{ppt} \sigma_{ppt} $ is also affected by temperature, similarly to the variation in shear modulus  $ G $.

The atomic numbers of Co, Cr, Fe, and Ni are sequentially adjacent; therefore, there is little difference in their atomic radii. Consequently, the atomic size mismatch within FCC FeCoCrNi HEAs is negligible. Hence, only Mo is recognized as a strengthening element. The solid-solution strengthening stress ( $ \sigma_{ss} $) caused by Mo is expressed as

 $$ \sigma_{\mathrm{ss}}=k_{\mathrm{Mo}}c_{\mathrm{Mo}}\sigma_{\mathrm{ss}}=k_{\mathrm{Mo}}c_{\mathrm{Mo}} $$ 

where  $ c_{Mo} $ is the concentration of solute Mo atoms and  $ k_{Mo} $ is the strengthening coefficient of the matrix (19.4 MPa/at%) (Kenji et al., 2002).

From the Hall–Petch relation, the grain boundary strengthening stress  $ \sigma_{GB} $ is given as

 $$ \sigma_{GB}=\frac{k_{HP}}{\sqrt{d}\sigma_{GB}}=\frac{k_{HP}}{\sqrt{d}} $$ 

where  $ k_{HP} $ is the Hall–Petch coefficient (taken as 226 MPa/ $ \mu $m $ ^{1/2} $ from the FeCoCrNiMn system) (Peng et al., 2022). Although there is no obvious difference in grain size between the samples with different Mo contents,  $ k_{HP} $ is influenced by both interstitial and substitutional elements. This leads to a correction term of 48[Mo] (where [Mo] is the Mo concentration in at%) (Kenji et al., 2002) for  $ k_{HP} $ in the Fe–Cr–Ni system, which is quite near the measured  $ k_{HP} $ value of 297 MPa/ $ \mu $m $ ^{1/2} $ for Mo1 (Dai et al., 2021). Therefore,  $ \sigma_{GB} $ is modified as follows:

 $$ \sigma_{GB}=\frac{(k_{HP}+48Mo)}{\sqrt{d}\sigma_{GB}}=\frac{(k_{HP}+48Mo)}{\sqrt{d}} $$ 

Figs. 14a and 14b compare the sum and contribution of each stress strengthening term to the yield strength during tensile deformation at room and high temperatures, respectively, which show good agreement with the experimental results. The most significant contribution is dislocation cell-coupled strengthening, which is characteristic of L-PBF-processed metals. Compared with MoO, an appropriate Mo addition ( $ \geq $7 at%) can markedly enhance the yield strength of FeCoCrNi-based HEAs, especially at high temperatures. This is because, although high temperatures can induce grain recovery, the solid-solution and precipitation strengthening induced by Mo can impede dislocation slip and exert a grain-boundary pinning effect.

However, the TEM characterization, ab initio calculations, and MD simulations reveal that excess Mo (e.g., 11.11 at%, Mo5) leads to excessive precipitation at grain boundaries. This significantly increases the SFE at high temperatures and hinders continuous dislocation slip after the initiation of yielding, culminating in a substantial decrease in the uniform elongation of samples with high Mo contents. Although the SFE of samples with low or no Mo (~2.4 at%, Mo1; 0 at%, Mo0) increases less than that of Mo5 at high temperatures, the fracture of these samples occurs before the tensile stress reaches the critical value for twinning, resulting in a significant loss of strength and toughness and compromising their high-temperature performance. Moreover, the critical twinning stress decreases within coarse grains (Cai et al., 2017; Wagner and Laplanche, 2023); therefore, the larger grain size of Mo3 is conducive to twinning. The dynamic Hall-Petch effect further enhances the strain-hardening ability (Liu et al., 2022). Consequently, an optimal Mo content (~7 at%, Mo3) can maintain the effects of solid-solution and precipitation strengthening while also inducing twinning in the later stages of deformation, which further enhances the dislocation hardening ability.

Fig. 14c depicts the distinctive mechanical performance of the L-PBF-processed FeCoCrNiMoₓ HEAs versus other alloys at 600 °C (see Fig. 2d and the Supplementary Material for further detail). By incorporating an optimal amount of Mo (7–11 at%), it is possible to regulate multiple strengthening and hardening mechanisms. These mechanisms include solid-solution strengthening, grain-boundary strengthening, precipitation strengthening, and twinning. This regulation facilitates enhanced strength–ductility synergy in Mo₃ at elevated temperatures.

### 4. Conclusions

In this study, we systematically studied the mechanical properties of L-PBF additively manufactured FeCoCrNiMoₓ HEAs with varying Mo contents at both room and elevated temperatures (25 and 600 °C, respectively). A multiscale analysis, incorporating SEM, EBSD, TEM, and quantitative simulations, was conducted to assess the microstructural evolution and tensile deformation and elucidate the underlying mechanisms. The conclusions drawn from this study are as follows:

1. The L-PBF-processed FeCoCrNiMoₓ specimens exhibit a near-defect-free matrix with distinct dislocation cell patterns. With the addition of Mo (2.44, 6.98, and 11.11 at%), σ-phase precipitation increases, accompanied by sharpening of the dislocation cell walls.

2. In conjunction with ab initio calculations, MD simulations, and TEM observations, the SFE of the FeCoCrNiMoₓ HEAs decreases with increasing Mo content and increases at elevated temperatures. As a result, twinning is more likely to occur at room temperature for all samples. However, at 600 °C, twinning is only observed for Mo3 owing to the increased SFE.

3. The addition of Mo to the FeCoCrNi matrix promotes both solid-solution and precipitation strengthening. By leveraging the versatility and rapid cooling of L-PBF, the introduction of an appropriate amount of Mo (7–11 at%) allows for precise microstructural control. This results in the simultaneous or sequential regulation of multiple strengthening mechanisms, including dislocation hardening, solid-solution strengthening, precipitation strengthening, hetero-deformation-induced strengthening, and twinning. Consequently, FeCoCrNiMo $ _x $ HEAs (x = 0.3–0.5) exhibit improved formability at room temperature and enhanced strength–ductility synergy at high temperatures. Specifically, the YS, UTS, and uniform elongation reach 580 MPa, 800 MPa, and 20%, respectively.

This study successfully demonstrates the relationship between the processing, microstructure, and mechanical properties of FCC FeCoCrNiMo $ _{x} $ HEAs at both room and elevated temperatures. Multiscale investigations, encompassing both experimental observations and modeling simulations, promote the understanding of the deformation mechanisms in Mo-doped HEAs. This understanding is based

<div style="text-align: center;"><img src="imgs/img_in_chart_box_109_111_547_442.jpg" alt="Image" width="40%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_98_109_979_917.jpg" alt="Image" width="80%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_552_117_977_437.jpg" alt="Image" width="39%" /></div>


<div style="text-align: center;">Fig. 14. Comparison of yield strength as a cumulative structural calculation of various stress hardening terms with experimental results: (a) 25 °C, (b) 600 °C. (c) Schematic of the deformation mechanisms of L-PBFed Mo3 HEAs achieving enhanced strength-ductility synergy at elevated temperature.</div>


on key microstructural characteristics such as stacking faults, twins, precipitates, and dislocation cell patterns, verifying the feasibility of using L-PBF to regulate the sequential activation of different strengthening mechanisms. Conventional methods such as SEM, TEM, and EBSD cannot capture the microstructure and twinning process at high temperatures. However, we have revealed this process through first-principles calculations and molecular dynamics simulations. By combining experimental observations with simulations, we have thoroughly analyzed the plastic deformation mechanisms of HEA alloys. This approach provides valuable insights for the development of new materials. This study provides valuable insights for structural HEAs to achieve synergistic high-temperature mechanical properties, thereby proving their significance and practicality in both scientific and engineering contexts.

### CRediT authorship contribution statement

Danyang Lin: Writing – original draft, Investigation, Funding acquisition, Conceptualization. Jixu Hu: Project administration, Methodology, Investigation, Conceptualization. Renhao Wu: Writing – review & editing, Visualization, Investigation, Funding acquisition. Yazhou Liu: Visualization, Investigation. Xiaoqing Li: Visualization, Investigation. Man Jae SaGong: Validation, Methodology, Investigation. Caiwang Tan: Project administration, Investigation. Xiaoguo Song: Supervision, Investigation, Funding acquisition. Hyoung Seop Kim: Writing – review & editing, Supervision, Methodology, Investigation, Funding acquisition.