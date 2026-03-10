# Origins of strength stabilities at elevated temperatures in additively manufactured refractory high entropy alloy

<div style="text-align: center;"><img src="imgs/img_in_image_box_1002_297_1059_353.jpg" alt="Image" width="4%" /></div>


Yongyun Zhang $ ^{a,b} $, Kaiping Yu $ ^{c} $, Bailiang Qin $ ^{a} $, Congrui Yang $ ^{a} $, Shulong Ye $ ^{d} $, Chuangshi Feng $ ^{b} $, Fuxiang Zhang $ ^{b} $, Di Ouyang $ ^{a} $, Lin Liu $ ^{e} $, Haibo Ke $ ^{b,**} $, K.C. Chan $ ^{a,*} $, Weihua Wang $ ^{b,f} $

 $ ^{a} $ Research Institute for Advanced Manufacturing, Department of Industrial and Systems Engineering, The Hong Kong Polytechnic University, China

 $ ^{b} $ Songshan Lake Materials Laboratory, Dongguan, 523808, China

 $ ^{c} $ Department of Mechanical Engineering, The University of Hong Kong, Pokfulam Road, China

 $ ^{d} $ Faculty of Materials Science, Shenzhen MSU-BIT University, Shenzhen, 518172, China

 $ ^{e} $ State Key Laboratory of Material Processing and Die & Mould Technology and School of Materials Science and Engineering, Huazhong University of Science and Technology, Wuhan, 430074, China

 $ ^{1} $Institute of Physics, Chinese Academy of Sciences, Beijing, 100190, China

#### ARTICLE INFO

Keywords:

Refractory high-entropy alloys

Additive manufacturing

Lattice distortion

Mechanical properties

Elevated temperatures

### A B S T R A C T

While refractory high-entropy alloys (RHEAs) show promising potential for extreme applications, those directly fabricated via additive manufacturing methods have been hindered by their inferior mechanical properties, particularly at high temperatures. In this study, we successfully produced a Hf-Nb-Ti-V RHEA using directed energy deposition (DED) technique, achieving satisfactory tensile properties across a wide temperature range. This was accomplished by inducing severe lattice distortions in the fabricated RHEA, which can be traced back to the local chemical fluctuations present in the newly fabricated RHEA and the significant atomic radius mismatch. Due to strong solute pinning, these factors contribute to the superior yield strength of the DED-fabricated RHEA across a wide temperature range. Furthermore, the elastic constants in the fabricated RHEA show a negligible temperature dependence, revealed by first-principles calculations, ensuring satisfactory strengths even at high temperatures. This alloy design strategy, which involves introducing significant lattice distortion and maintaining the temperature-low sensitivity of the elastic moduli, opens up new possibilities for directly fabricating RHEAs with superior high-temperature properties.

### 1. Introduction

Unlike the traditional alloying design concept, which involves one principal metallic element doped with minor alloying elements, the high-entropy alloy (HEA) design paradigm does not rely on a unique base metal [1,2]. This approach allows for creating HEAs or multi-principal element alloys (MPEAs) with remarkable mechanical [3,4] and superior electrochemical properties [5]. HEAs composed of refractory elements demonstrate exceptional mechanical properties under elevated temperatures [6], far surpassing Ni-based superalloys [7,8]. This not only presents opportunities for advanced applications, from aerospace to nuclear reactors [7,9] but also broadens the compositional space for advanced alloy design [10]. For advanced structural materials applications, refractory high-entropy alloys (RHEAs) typically exhibit satisfactory mechanical properties at both room temperature (RT) and high temperatures [6,11]. A representative of the former is HfNbTiZrTa RHEA [12], and the latter is MoNbTaW RHEA [8]. However, these alloys, despite their impressive properties at their respective application temperatures, are seen to perform poorly at unaccommodated temperatures [8,12]. For instance, HfNbTiZrTa RHEA exhibits significantly deteriorated tensile properties when the applied temperature exceeds a certain threshold [12,13], and MoNbTaW RHEA rarely shows tensile ductility, especially at room temperature [14]. This necessitates the development of novel RHEAs that can meet the wide temperature range requirements.



To meet the potential engineering applications of RHEAs, selection of fabrication processes is crucial. Generally, casting  $ [3,4] $ and powder metallurgy (PM)  $ [15] $ methods are the primary techniques used for

manufacturing RHEAs, but they have inherent drawbacks. For instance, as-cast RHEAs undergo homogenization-rolling-annealing procedures [3,4], significantly lengthening the manufacturing period. Although PM methods offer the potential to directly fabricate RHEAs with complex geometries [16], these processes often introduce impurities or lead to severe matrix decomposition [15] even if the designed RHEA has a single body cubic crystal (BCC) structure. Laser-aided directed energy deposition (DED) technologies, known for their high degree of freedom and precision, enable the customization of products with complex geometries while saving raw materials and time [17,18]. However, successfully fabricating RHEAs with superior mechanical properties has been challenging over the past decade [19-26]. Numerous attempts have been made to fabricate RHEAs via AM methods but often resulted in a variety of defects and thus poor RT mechanical performance [19-26] much less the tensile properties at elevated temperatures. Recently, several efforts were proposed like phase engineering [20], the solid solution treatment [27] as well as laser energy regulation [28] to enhance RT tensile properties of DED-fabricated RHEAs by controlling the formation of harmful phases. Additionally, selecting alloys with an inherent ductile nature can also facilitate the fabrication of RHEAs with enhanced tensile strength and ductility compared to their as-cast counterparts [10]. However, it is clear that there is still data blank in tensile properties across a wide temperature range of AM-fabricated RHEAs.

Among the well-known core effects in HEAs, lattice distortion is often credited for impressive properties such as the Elinvar effect [29], high strength at elevated temperatures [7], and strength-ductility synergy in RHEAs [3,30,31]. Whether it's the presence of oxygen in HfNbTiZr RHEA [32] or the local chemical order in Ti-based MPEA [3] that resolves the strength-ductility trade-off dilemma, or even the long-range chemical fluctuations [4], the influence of local lattice distortion (LLD) on the mechanical properties of BCC type alloys is significant. Customizing LLD in RHEAs is crucial for enabling remarkable properties, particularly superior high-temperature strength. RHEAs containing Zr and Hf have been shown to cause a significant atomic radius mismatch [9,33], resulting in a larger LLD in these alloys compared to face-centered cubic (FCC) type HEAs [34]. Additionally, introducing elements with low temperature-dependent elastic constants, such as Nb and V [7], can enable a stable yield strength to overcome heat softening under elevated temperatures [8,35]. Alloying methods, such as the addition of Ti, are effective in improving the ductility of brittle RHEAs [36]. Designing LLD in RHEAs to achieve exceptional strength under elevated temperatures while maintaining ductility is significant in additive manufacturing of RHEAs. Despite the study of the relationship between lattice distortion and friction stress in Nb-contained high-entropy alloys [37], it is crucial to fully understand the mechanisms for the superior mechanical properties induced by LLD at elevated temperatures.

In this study, we successfully fabricated a Ti42Hf21Nb21V16 (referred to as T42) RHEA using a laser-engineered net shaping (LENS) approach, also known as a laser-aided DED technology, via incorporating an extremely high energy input for remelting. This alloy exhibits superior tensile properties at room temperature and even at elevated temperatures. Furthermore, we examined the local chemical complexity in the AM-fabricated RHEAs and quantitatively investigated the LLD using pair distribution function analysis of the x-ray total scattering data. We also employed simulation methods, including first-principles calculations and crystal plasticity finite element modeling, to study the basic physical parameters and mechanical response under varying temperatures. Our findings pave the way for the direct manufacturing of RHEAs with superior mechanical properties and provide insights into the mechanical responses of these RHEAs under extreme conditions.

## 2. Experimental section

#### 2.1. Sample preparation

The T42 RHEA sample was additively manufactured using a mixture of pure Ti, Hf, Nb, and V powders (all with purities exceeding 99.95%), as shown in Fig. 1 a, with a nearly even distribution, illustrated by the corresponding elemental maps (Fig. 1 b). The particle size of the powder mixture was determined via a particle analyzer (Malvern Mastersizer 3000), giving an average particle size of ~81 μm (Fig. 1 c), indicating the acceptable flowability of the powder mixture used for LENS. In addition, we also applied x-ray diffraction (XRD, λ = 1.54 Å for Cu Kα) testing, given in Fig. 1 d, showing the phase structure of well-mixed elemental powders, which were prepared using plasma rotation electrode atomization technology. During the LENS process, a remelting procedure (detailed in Ref. [10]) involving ultra-high energy input was performed to maintain a uniform elemental distribution and prevent the presence of un-melted elemental powder, which could occur due to the significant differences in melting points among these elemental powders. Argon was introduced into the LENS machine's (Optomec LENS MR-7) working chamber to maintain a low oxygen content (below 200 ppm). The fabrication process involved a scanning speed of 5 mm/s, hatching space of 381 μm, working laser power of 550 W, remelting power of 800 W, and a layer thickness of 200 μm. After the LENS procedure, a bulk RHEA sample measuring 70 × 12 × 5 mm was obtained for further testing, as displayed in Fig. 1 e.

### 2.2. Mechanical tests

The tensile tests were conducted on the as-deposited samples at various temperatures, including RT, 673 K, 773 K, 873 K, and 1073 K, at a strain rate of  $ 1 \times 10^{-3} \, s^{-1} $. The tests were carried out using a Zwick-Roell Proline universal testing machine equipped with a heating chamber, and strain evaluation was performed using digital image correlation (DIC). The tensile bar used in the experiments had a gauge length of 6 mm and a thickness of 1 mm. Prior to the hot tensile experiment, the tensile bar was preloaded at 30 N to compensate for thermal expansion during the heating process. A heating speed of 10 K/s was employed to reach the target temperature, and the hot tensile test commenced after a 10-min thermal insulation period at the target temperatures in the heating chamber.

### 2.3. Microstructural and structural characterization

We utilized scanning electron microscopy (SEM, Verios 5 UC, Thermo Fisher) and electron back-scattered diffraction (EBSD, C-swift, Oxford) to analyze the microstructure of LENS-fabricated RHEA. The SEM specimens, including the deformed samples, were ground with 2000-grit SiC paper, polished with 1 µm micro-sized polycrystalline diamond solutions (Struers), and then finished with a finer polishing using a 50 nm sized SiO₂ particle solution (OPS, Struers). Subsequently, the samples underwent ion polishing by an Ion Beam Etching machine (EM TIC 3X, Leica) at 5 kV for 1 h. Additionally, transmission electron microscopy (TEM, Talos F200X, Thermo Fisher) was employed to investigate the microstructure at the nano-scale, with samples prepared via focus-ion beam (FIB, Helios 5 UX). The atomic structure of the as-deposited RHEA was characterized using an aberration-corrected TEM (Spectra 300, Thermo Fisher) at a working voltage of 300 kV, while deformed samples were observed in Talos F200X to study dislocation evolution after tensile tests at different temperatures. The atomic chemical composition was analyzed using 3D atom probe tomography (APT, LEAP 6000 XR), with needle-shaped specimens sampled by FIB (Helios 5 UX) using the milling and lift-out method. The needle-shaped APT sample was examined in voltage mode (detection efficiency 0.5 %) at a temperature of 50 K with a pulse repetition rate of 200 kHz and 20 %, respectively. The collected data was then used to reconstruct the 3D

<div style="text-align: center;"><img src="imgs/img_in_image_box_88_116_1104_852.jpg" alt="Image" width="85%" /></div>


<div style="text-align: center;">Fig. 1. Experimental details for T42 alloy fabrication. a, The powder morphologies of mixed powder with b, corresponding elemental maps. c, Powder size distribution map. d, The XRD profiles of mixture of used elemental powder. e, the LENS fabrication procedure.</div>


elemental distribution using IVAS software. The phase composition of the as-deposited RHEA was investigated via x-ray diffraction (XRD) and selected area electron diffraction (SAED) in TEM equipped with energy-dispersive X-ray (EDX). Additionally, atomic pair distribution function (PDF) analysis was conducted using the X-ray total scattering data collected on a laboratory X-ray scattering instrument (SmartLab, Rigaku) equipped with a rotating anode silver target ( $ \lambda = 0.56 \AA $ for Ag  $ K\alpha $), and then extracted from the program of PDFGetX3 [38]. During the data collection procedure, the transmission setup utilized a capillary sealed with the sample and subtracted the data from the empty capillary to obtain the scattering signal of the detected sample. The acquired data were processed using Fourier transform on the normalized X-ray scattering function ( $ F(Q) $),  $ Q = 4\pi \cdot \sin \theta / \lambda $, to obtain the respective PDF (G (R)). After obtaining the required PDF, the PDFgui package [39] was used to fit different structure models of the as-fabricated RHEA.

### 2.4. High temperature oxidation experiments

For investigating the failure mechanism of the as-fabricated T42 RHEA, we carried out 1073 K oxidation experiments. The oxidized samples were cut into dimensions of  $ 10 \times 10 \times 4 $ mm via an electrical discharge cutting machine and then underwent grinding as well as polishing procedures. The samples were oxidized in an open-air tube furnace. The weights of the oxidized samples processing at 1h, 3h, 6h, 12h, 24h, 48h, 72h, 96h as well as 120h were collected by a precise balance (Sartorius SQP), and the corresponding microstructure and phase composition were achieved via SEM (Verios 5 UC) and XRD (Smartlab, Cu  $ \lambda = 1.54 \AA $) experiments.



#### 2.5. First-principles calculations

To determine the temperature dependence on the physical moduli in the target alloy system, we utilized the Cambridge Sequential Total Energy Package (CASTEP) [40] to conduct first-principles calculations using the virtual crystal approximation (VCA) method, which has been demonstrated to be effective in studying the fundamental physical properties of HEAs [41]. Within the CASTEP package, the generalized gradient approximation (GGA) with Perdew-Burke-Ernzerhof (PBE) was employed for geometric structure optimization, utilizing TPSD algorithms. The OTFG norm serving pseudopotential was employed without selecting spin polarization. We customized the energy cutoff to 1200 eV and utilized k-points of  $ 20 \times 20 \times 20 $ implemented on the conventional cell, setting the maximum total energy loss to  $ 1 \times 10^{-5} $ eV-atom $ ^{-1} $. Other relevant settings included ensuring the maximum forces on single atoms were less than 0.03 eV-Å $ ^{-1} $, atom placement was less than 0.001 eV-Å $ ^{-1} $, and the total stress tensor order was chosen as 0.05 GPa.

### 3. Experimental and simulation results

#### 3.1. Microstructure of as-fabricated RHEA

In the fabrication of RHEAs through additive manufacturing, early

attempts often encountered issues with unmelted elemental powders [19,22,23], which significantly affected the properties of the manufactured RHEAs. In this study, we applied a remelting procedure to fabricate the T42 RHEA, and the microstructure of which is shown in Fig. 2. Fig. 2 a and b display the EBSD results collected from the upper (XY) and lateral (XZ) planes, respectively. These different planes reveal distinct grain morphologies; the XY plane shows equiaxed grains with a mean size of 200 μm, while the lateral plane exhibits a columnar crystal morphology with nearly double the mean size (Fig. 2 a (i) and b (i)). The microscale strain, reflected in the Kernel Average Misorientation map (Fig. 2 a (ii) and b (ii)), shows no significant differences in microstrain distribution across different fabrication directions in the selected RHEA after the AM procedure. Notably, a single BCC phase structure was formed after the AM procedure (Fig. 2 a (iii) and b (iii)), which is supported by the non-equilibrium phase diagram (see Supplementary Information (SI), Fig S1) obtained via the CALPHAD method. To ensure evenly distributed alloying elements, we simultaneously acquired EDS elemental maps (Fig. 2 c), which eliminated the formation of unmelted elemental powder when applying the remelting procedure during the fabrication of the selected RHEA. After post-processing the IPF figure collated from the XY surface, we obtained the corresponding pole and inverse pole figure density maps (Fig. 2 d and e), indicating the formation of a <001>//(110) texture after additive manufacturing [10].

We then examined the nano-structure of the as-fabricated T42 RHEA, with the results presented in Fig. 3. In Fig. 3 a (i), contrast differences are observed in the as-fabricated T42 RHEA. However, the corresponding EDS mappings (Fig. 3 a (ii)) indicate that there are no significant differences between the composed constituents. Subsequently, under HRTEM, the contrast difference is still evident, as displayed in Fig. 3 b (i). By amplifying the corresponding area, we obtained the atomic map, shown in Fig. 3 b (ii), indicating the differences in the formation of lattice structure in the as-fabricated T42 alloy. We then utilized the Geometric Phase Analysis (GPA) method [42] to study the lattice-scale lattice strain based on the atomic scale map (Fig. 3 c (i)), as depicted in Fig. 3 c (ii), revealing the presence of significant lattice strain induced by lattice distortion [43,44]. Based on the FFT result (Fig. 3 c (ii)) through Fig. 3 c (i), we collected the atomic scale map from the [001] axis of the as-fabricated T42 alloy. The formation of lattice distortion originates from atomic radius and shear modulus mismatches [45], which are also promoted by local chemical fluctuations, as given in Fig. S 2 (SI). Consequently, we conducted an APT experiment, with the results presented in Fig. 3 d. The APT map (Fig. 3 d (i)), which excerpted the 20 at. % V isocomposition, supports the formation of nano-scale composition heterogeneity. Additionally, by collecting the corresponding compositional proximity histogram of the selected particle in Fig. 3 d (i), the presence of LCFs in the as-fabricated T42 alloy is evident. It is important to note that, due to the sampling size for the APT experiment, the acquired elemental concentrations differ from the microcosmic EDS results, indicating the presence of compositional heterogeneity.

The EBSD phase map (Fig. 2 a(iii)) confirms the formation of a single BCC phase in the as-fabricated T42 alloy. Additionally, we conducted an XRD experiment to investigate its phase structure, as illustrated in Fig. 4. The XRD profile (Fig. 4 a) supports the formation of a single BCC phase in the as-fabricated RHEA. As previously mentioned, local lattice strain is produced in the as-fabricated T42 RHEA. To demonstrate the presence of local lattice strain/distortion, the atomic PDF, acquired via Fourier transformation from the total scattering data, is presented in Fig. 4 (b), providing inter-atomic distances in real space [46]. Our PDF curve exhibits a similar characteristic to the Hf-contained BCC HEA [9], indicating the accuracy of the total scattering data collected using the Ag target ( $ \lambda = 0.559 \AA $). By fitting the PDF data, we obtained a fitting curve in Fig. 4 b (red line), which yields a lattice constant of 3.32626  $ \AA $. However, an overlap of the first and second atomic shell was also observed in our Hf-containing RHEA, as shown in Fig. 4 b (i), indicating a strong local lattice distortion (LLD) caused by the severe motion among neighboring atoms [47]. We fitted different r regions separately to reveal the LLD, which are [48]: 1) local range (one unit cell < 4  $ \AA $); 2) long-range (3 unit cell) as well as 3) intermediate range, as shown in Fig. 4 b (i-ii). As the LLD can be reflected as the shift of the PDF peak [9], the local strain can be obtained via [9,48]:



 $$ \varepsilon=\frac{\left|a_{fit}-a_{ave}\right|}{a_{ave}} $$ 

where  $ a_{fit} $ is the fitting lattice constant in different r regions while  $ a_{ave} $ denotes the average lattice constant in the whole r range. Consequently, we obtained the LLD in different regions, as shown in Fig. 4 c, indicating a local range lattice strain of 3.68 %, much higher than that in the FCC HEAs [49] but also slightly larger than the values in Hf-/Zr- containing RHEA [9].

### 3.2. Mechanical properties under elevated temperatures

To obtain the mechanical responses of the as-fabricated T42 alloy, we conducted tensile tests at different temperatures, which would be more valuable than compressive tests for evaluating its engineering application potential [20], with the results presented in Fig. 5 (a). The AM-fabricated T42 alloy exhibited superior strength and ductility synergy, with a yield strength of approximately 1030 MPa and a fracture strain of 22.5 %, surpassing the reported AM-fabricated RHEA [10]. When the tensile temperature was increased to 673 K, the yield strength of the as-fabricated T42 alloy decreased to ~681 MPa, while the fracture strain increased to 27.8 % in our study. According to the Considère criteria [50], strain hardening was observed during the high-temperature tensile test. Upon further increasing the temperature to 773 K, a decrease in the yield strength to ~661 MPa was observed in the as-fabricated T42 alloy. Additionally, the fracture strain decreased to ~16.8 % compared to the tensile curve obtained at 673 K. Following the tensile test at 873 K, a slight decrease (approximately 25 MPa) in the yield strength and a significant decrease in the fracture strain (~7.5 %) were observed compared to the curves obtained at lower temperatures. It should be mentioned that the as-fabricated T42 alloy was completely disabled at that temperature when the tensile temperature was raised to 1073 K, and valid results could not be obtained. Additionally, we compared the yield strength versus temperature of the as-fabricated T42 alloy to the as-cast RHEAs [51–55] and the AM-fabricated superalloy [56–58] and other alloys with reported high temperature tensile properties [59,60], due to the absence of reported data in the AM-fabricated RHEAs, as shown in Fig. 5 b. The as-fabricated T42 alloy exhibited superior yield strength at room temperature among those reported alloys. With increasing working temperature, the tensile yield strength slightly decreased but remained competitive among the AM-fabricated superalloys [56–58], although it was negligibly lower than the as-cast HfNbTiZrTa alloy [54,55]. The latter is generally included in the high melting point alloying element Ta, enabling a higher melting point [61] compared to our target alloy. However, under a high-temperature tensile test, especially above 823 K, matrix decomposition would occur [12], significantly deteriorating both strength and ductility in the HfNbTiZrTa alloy [13,54,55]. Although there have the Ni-based superalloys with even superior mechanical performance at higher temperature than our alloy fabricated alloy, successful fabrication of superalloys with superior mechanical properties by AM is still a long way to go [56–58]. In conclusion, although our as-fabricated T42 alloy has a relatively lower melting point, it still exhibits superior mechanical properties at elevated temperatures.

Following the tensile tests, we examined the fractured surfaces and the external surfaces parallel to the tensile direction using SEM, as depicted in Fig. 6, which illustrates the fracture morphologies under different temperatures. After the RT and 673 K tensile tests, complete ductile fracture surfaces were observed, as shown in Fig. 6 a (i-ii), characterized by the formation of dimples. When the tensile temperature was increased to 773 K, surface cracks were observed (Fig. 6 a (iii)),

<div style="text-align: center;"><img src="imgs/img_in_image_box_94_106_1092_1454.jpg" alt="Image" width="83%" /></div>


<div style="text-align: center;">Fig. 2. The microstructure of LENS-fabricated T42 RHEA. a (i-ii), The IPF, KAM and phase figures on XY plane. b (i-ii), The IPF, KAM and phase figures on XZ plane. c, The corresponding elemental distribution maps. d and e, the pole figures and inverse pole figures converted from the XY plane.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_89_114_1108_1040.jpg" alt="Image" width="85%" /></div>


<div style="text-align: center;">Fig. 3. The nano-scale structure of as-fabricated T42 RHEA. a (i-ii), The bright field (BF) TEM figure with corresponding elemental distribution maps. b (i), BF TEM figure under a higher resolution and (ii) atomic resolution image with corresponding FFT image showing the presence of lattice distortion. c (i-ii), high resolution atomic image with corresponding local strain distribution map collected along z = [001]. d(i-ii), APT image which excerpt at 20 at. % V isocomposition surface and the corresponding regional proxigram acquired from (i).</div>


and most of the fracture surface had dimples, with the presence of cleavage fracture characteristics under the surface cracks. Upon further increasing the tensile temperature to 873 K, a few dimples were observed, but most of the fracture surface exhibited river patterns (Fig. 6 a (iv)), indicating the formation of quasi-cleavage fracture under that particular temperature and external stress. Regarding the observation of the external surface, as shown in Fig. 6 b, both the RT and 673 K tension samples exhibited large plastic regions, composed of highly deformed grains with shear bands and a high density of dislocations. In contrast, a small plastic deformed region was observed in the 873 K tension sample, with surface cracks occurring during the tensile test. As the external surfaces were prepared by grinding and polishing, surface cracks were rarely observed in the 773 K tension sample, which can be seen from the front fracture surface in Fig. 6 a (iii).

#### 3.3. Deformed microstructure under elevated temperature

To further investigate the deformed microstructure near the fracture cross section of the as-fabricated T42 samples after tension under elevated temperatures, we conducted EBSD experiments, the results of which are presented in Fig. 7. In the EBSD IPF figures, we observed extensive shear bands, rather than the formation of deformed twin structures [20], formed under the RT tensile test. However, the amount of shear bands was noticeably reduced in samples tensioned under elevated temperatures. Additionally, we utilized Kernel Average Misorientation (KAM) maps to study the degree of deformation or the distribution of geometrically necessary dislocations [62]. From the KAM figures, it was evident that highly deformed regions near the grain boundaries or the shear bands exhibited a high density of dislocations. As the twinning-induced plasticity effect [10] was eliminated in our

<div style="text-align: center;"><img src="imgs/img_in_chart_box_82_117_584_342.jpg" alt="Image" width="42%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_592_112_1104_342.jpg" alt="Image" width="42%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_81_346_585_576.jpg" alt="Image" width="42%" /></div>


<div style="text-align: center;">r(A)</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_596_355_1092_584.jpg" alt="Image" width="41%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_81_585_583_835.jpg" alt="Image" width="42%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_592_592_1099_835.jpg" alt="Image" width="42%" /></div>


<div style="text-align: center;">Fig. 4. Precise XRD results. a, XRD profile of as-fabricated T42 RHEA. b, The PDF curve fitted via PDFgui package a different r regions (i-ii). c, calculated local lattice strain derived from PDF fitting.</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_81_931_519_1232.jpg" alt="Image" width="36%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_530_941_1108_1226.jpg" alt="Image" width="48%" /></div>


<div style="text-align: center;">Fig. 5. The tensile properties of as-fabricated T42 alloy. a, typical tensile curves of as-fabricated T42 alloy tensioned at different temperatures. b, Yield strength as a function of tested temperatures in comparison to other as-cast RHEAs [51–55] and AM-fabricated alloys with reported hot tensile properties [56–60].</div>


study, we also examined the phase structure of the deformed surfaces, which indicated that no phase transformation occurred under tensile deformation, regardless of the temperatures applied in the study.

We then investigated the dislocation evolution during deformation under different temperature tensile tests using TEM. In Fig. 8 a (i), the TEM bright field picture of the RT tensile test reveals the presence of substantial planar slip bands and dislocation walls, while wavy slips were observed in that region with pinned dislocations after the RT tensile test (Fig. 8 a (ii)). The corresponding SAED pattern confirms that no phase transformation occurred after the RT tensile test, and the collected zone axis was [1 1 1] (Fig. 8 a (ii)). For the 673 K tensioned T42 sample, as shown in Fig. 8 b, we also observed bits of slip bands, dislocation walls, and pinning effects in the sample tensioned at that temperature. Additionally, the deformed structure after the 873 K tensile test, as depicted in Fig. 8 c, indicates tangled dislocations, dislocation jog, and dislocation loops, with the pinning effect still present in the



<div style="text-align: center;"><img src="imgs/img_in_image_box_89_112_1106_690.jpg" alt="Image" width="85%" /></div>


<div style="text-align: center;">Fig. 6. The fracture morphology observation in SEM. a (i-iv), Front fracture morphologies with corresponding enlarged microstructure of samples tensioned under RT, 673 K, 773 K and 873 K respectively. b (i-iv), External deformed microstructure of RT, 673 K, 773 K and 873 K tensioned T42 alloy.</div>


high-temperature deformed nanostructures. Based on the high-resolution TEM picture (Fig. 8 c (iii)) and its corresponding inverse fast Fourier transform (iFFT) (Fig. 8 c (iv)), we can assert that the combined effect of edge and screw dislocations was at work during the high-temperature deformation process. To verify the presence of dislocation loops and eliminate the formation of oxides after high-temperature tensile tests, the EDS maps of Fig. 8 c (ii) are shown in Fig. 8 d, indicating evenly distributed compositions even after high-temperature tensile tests.

#### 3.4. High temperature oxidation property

Despite the superior mechanical properties exhibited by the as-fabricated T42 alloy under elevated temperatures, it proved to be not applicable under a tensile test at 1073 K. Consequently, we conducted a long-term (120-h) oxidation experiment under atmospheric conditions at 1073 K. After a 1-h oxidation test, we observed the oxidized surfaces of the as-fabricated T42 sample, as shown in Fig. 9 a, where surface cracks were present in the oxidation layer. Subsequently, we collected the elemental distributions on the oxidation layer, as depicted in Fig. 9 b, indicating the formation of oxides of corresponding constituents in the T42 alloy. The mass gain of oxidized samples under different processing times (1 h, 3 h, 6 h, 12 h, 24 h, 48 h, 72 h, 96 h, as well as 120 h) are shown in Fig. 9 c, clearly demonstrating a nearly linear increase in mass gain with an increase in processing time. Additionally, we conducted XRD tests to study the phase evolution of the oxides of the AM-fabricated T42 alloy (see Fig. 9 d), indicating that prolonging the processing time would not affect the oxide species, only the number of oxides. After 120 h of high-temperature oxidation, we observed the macroscopic features as well as the microstructure of the as-fabricated T42 alloy in Fig S 3 a and b (SI), revealing severe dehiscence on the oxidation layer, while the elemental distribution of the oxidation layer (Fig S 3 c) showed no significant difference compared to the short-term oxidized T42 alloy.

#### 3.5. Basic physical properties of selected RHEA at elevated temperatures

In our study, we utilized the EOS approach (for details see Note 2 in SI) to obtain the thermal dynamic parameters of the selected RHEA (as shown in Fig S 4 in SI) and then obtained the temperature dependence of the lattice constant as listed in Table 1. After the calculation, the lattice constant of the T42 alloy was determined to be 3.3176 Å, which is very consistent with the fitted PDF result of 3.32626 Å, indicating that an appropriate parameter setting was applied in this calculation procedure. Based on the calculated lattice constants, we applied first-principles calculations to obtain the independent elastic constants, C11, C12, and C44, which also meet the requirements of the Born-Huang mechanical stability criterion [63], as expressed in the following equation:

 $$  C_{11}-C_{12}>0,C_{11}+C_{12}>0,C_{44}>0 $$ 

Fig. 10 shows the basic physical properties of the T42 alloy at corresponding temperatures. The linear increase of the lattice constant was found as a function of temperature, as illustrated in Fig. 10 a. The selected RHEA exhibits a degree of anisotropy which is less than 1 (see Fig. 10 b) among the test temperatures, indicating the loss of anisotropy at higher temperatures. The independent elastic constants of C11 and C12 slightly increased with elevated temperatures, while C44 slightly decreased, resulting in a slight decrease of Young's moduli and shear moduli (seen Fig. 10 c and d) in the selected RHEA and a weak temperature dependence on the basic moduli of the selected RHEA. By applying similar calculations on the pure constituents in Ti-based RHEA, we showed the temperature-dependent Young's and shear moduli in Fig. 10 c and d, which illustrates a weak temperature-dependence on E and G in those pure metals, similar to the results given in the study by Feng et al. [7].

### 3.6. CPFEM results

To verify the accuracy of the calculated moduli as a function of

<div style="text-align: center;">IPF</div>


<div style="text-align: center;">a</div>


<div style="text-align: center;">KAM</div>


<div style="text-align: center;">Phase</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_83_106_1106_1079.jpg" alt="Image" width="85%" /></div>


<div style="text-align: center;">b</div>


<div style="text-align: center;">C</div>


<div style="text-align: center;">d</div>


<div style="text-align: center;">Fig. 7. The EBSD deformed microstructure under elevated temperatures. a-d, RT, 673 K, 773 K, 873 K, respectively.</div>


temperature, we modelled the tensile properties of the as-fabricated T42 alloy using the DAMASK (Düsseldorf Advanced Materials Simulation Kit) package [64] and a dislocation-based crystal plasticity constitutive model (Details in Note 2, SI). We utilized the actual 3D EBSD construction (Fig. 11 a) to create polycrystalline representative volume elements (RVEs) with near-identical experimental morphologies (Fig. 11 b) via the DEREAM3D package [65]. Taking into account the presence of preferable orientations formed in the as-fabricated T42 alloy (Fig. 2 d), we assigned near-identical preferable orientations in our RVEs, as shown in Fig. 11 c. The RVEs used for CPFEM were meshed into  $ 60 \times 60 \times 60 $ elements, containing 27 grains, and a tensile rate of  $ 0.001 \, s^{-1} $ was applied in the X-direction during hot-tensile simulations. By fitting the experimental tensile curves and simulations, as illustrated in Fig. 11 d, we introduced the average absolute relative error (AARE) and the correlation coefficient (R) to verify the reliability of the CPFE model used in this study, as follows [66]:

 $$ A A R E(\%)=\left\{\frac{1}{N}\sum_{i=1}^{N}\left|\frac{E_{i}-P_{i}}{E_{i}}\right|\right\}\times100 $$ 

 $$ R=\frac{\sum\limits_{i=1}^{N}\left(E_{i}-\overline{E}\right)\left(P_{i}-\overline{P}\right)}{\sqrt{\sum\limits_{i=1}^{N}\left(E_{i}-\overline{E}\right)^{2}\sum\limits_{i=1}^{N}\left(P_{i}-\overline{P}\right)^{2}}} $$ 

where N denotes the data points,  $ E_i $ and  $ P_i $ are stress values of experimental and simulation results, respectively, while  $ \overline{E} $ and  $ \overline{P} $ refer as average value obtained from experiment and simulation, respectively. We summarized the AARE and R values in Table 2, showing small AAREs but high R values in our simulations, indicating a strong correlation between experimental and simulation results. Additionally, we obtained the temperature dependence on the constitutive parameters, listed in

<div style="text-align: center;"><img src="imgs/img_in_image_box_97_110_1108_989.jpg" alt="Image" width="84%" /></div>


<div style="text-align: center;">Fig. 8. Nano-scale deformed structure in TEM. a (i-ii), the RT deformed BF image with (iii) corresponding SAED pattern collected along Z = [111] axis. b, 673K deformed nano structure showing. c, dislocation structure in the deformed T42 alloy under 873 K, with HRTEM given in (iii) and the corresponding iFFT figure indicating the presence of mixed dislocation structure in the deformed sample. d, the EDS elemental mappings of 873 K deformed structure.</div>


Table 3, and the activation energy for glide evolute as a function of temperature [67], which are  $ 3.53 \times 10^{-19} $ J (RT),  $ 2.3 \times 10^{-19} $ (673 K),  $ 2.2 \times 10^{-19} $ (773 K) and  $ 2.1 \times 10^{-19} $ (873 K), respectively. The well-fitted experimental and simulation results indicate the accuracy of the DFT calculations and show the way for directly predicting the mechanical response of novel alloys.

### 4. Detailed discussion

### 4.1. Microstructure and origins of lattice distortion in RHEAs

To achieve an evenly distributed macro-scale RHEA, we utilized a remelting procedure to fabricate the chosen RHEA. In the AM-fabricated alloys, the highest thermal conductivity coincides with the BD [68], which can instigate the formation of columnar grains along the BD. This favors the orientation of the <001> direction [69,70], and the corresponding results are displayed in Fig. 2. Despite the even compositional distribution in the AM-fabricated T42 RHEA observed in Fig. 3 a (ii), local chemical fluctuations are present at the atomic level (Fig. 3 d), even deviating from the nominal composition. The formation of LCFs has been proven to be an effective barrier for dislocation motion, thereby enabling the strength-ductility synergy in BCC-type RHEAs [71]. The formation of LCF can be determined by the negative mixing enthalpy of the compositional constituents [4] In our study, the V element has a relatively higher negative mixing enthalpy with other compositional constituents [4], resulting in atomic segregation in the as-fabricated T42 alloy, as shown in Fig. 3 d.



We also examined the LLD produced in the AM-fabricated T42 alloy. Although the XRD method is effective for investigating lattice distortion by reducing peak intensity [72,73], the peak intensity and width are still influenced by the crystal microstructure, size, and textures [74,75]. Due to the presence of LCFs, commonly reported in Hf-containing RHEAs [71], fractal-like lattice distortion was observed in HRTEM and confirmed by the FFT patterns of their corresponding selected areas (Fig. 3 b(ii)) and the atomic strain map obtained via the GPA method (Fig. 3 c (ii)), commonly used for studying LLD in other HEAs [76,77]. Conversely, PDF converted from the diffraction total scattering data can provide valuable inter-atomic positions [46]. Tong et al. [9] found that

<div style="text-align: center;"><img src="imgs/img_in_image_box_86_111_1105_972.jpg" alt="Image" width="85%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_86_381_469_689.jpg" alt="Image" width="32%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_94_693_501_975.jpg" alt="Image" width="34%" /></div>


<div style="text-align: center;">Fig. 9. 1073 K oxidation results. a, The oxidation layer morphology after 1h oxidation test. b, Amplified microstructure as well as the corresponding elemental distribution maps showing the presence of oxides of corresponding constituents. c, the mass gain as a function of processing time. d, XRD profiles of oxidized T42 alloy under different processing time.</div>


<div style="text-align: center;">Table 1 DFT calculated results of T42 alloy.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Temperature/K</td><td style='text-align: center; word-wrap: break-word;'>RT</td><td style='text-align: center; word-wrap: break-word;'>673 K</td><td style='text-align: center; word-wrap: break-word;'>773 K</td><td style='text-align: center; word-wrap: break-word;'>873 K</td><td style='text-align: center; word-wrap: break-word;'>1073 K</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Lattice constant/ $ \mathring{A} $</td><td style='text-align: center; word-wrap: break-word;'>3.3176</td><td style='text-align: center; word-wrap: break-word;'>3.3293</td><td style='text-align: center; word-wrap: break-word;'>3.3321</td><td style='text-align: center; word-wrap: break-word;'>3.3350</td><td style='text-align: center; word-wrap: break-word;'>3.3408</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Young&#x27;s modulus/GPa</td><td style='text-align: center; word-wrap: break-word;'>105.99</td><td style='text-align: center; word-wrap: break-word;'>106.26</td><td style='text-align: center; word-wrap: break-word;'>106.18</td><td style='text-align: center; word-wrap: break-word;'>106.03</td><td style='text-align: center; word-wrap: break-word;'>105.55</td></tr></table>

Zr- and Hf-containing RHEAs have an overlap of the 1st and 2nd atomic shells, similarly depicted in Fig. 4 b (i), indicating the presence of large LLD in these alloys. Compared to the increase of chemical complexity in RHEAs, inducing atomic size mismatch seems to be more effective in increasing LLD, such as adding Hf or Zr large atomic radius elements [9]. We fitted different regions in our PDF curve (refer to Fig. 4 b), as the PDF peak position is a function of the lattice constant [9]. Ultimately, a significantly higher lattice strain/distortion of 3.68 % than that in previous Hf- and Zr-containing RHEAs was obtained (see Fig. 4 c), resulting from the solution interstitial atoms [10], which indicates the presence of large LLD in the as-fabricated T42 HEA.

#### 4.2. The mechanical responses at different temperatures

The lattice distortion in traditional alloys is well-established, typically involving solute atoms in the matrix, resulting from the atomic size and elastic modulus mismatch [45,78], which can distort the local elastic field and hinder dislocation movement [75] to ensure a higher yield strength. In RHEAs, the solute and solvent atoms show no significant differences [1], hence the accumulated contribution by lattice distortion and modulus mismatch to the solid strengthening in RHEAs is considered [78]. RHEAs composed of high melting point elements exhibit excellent structural stability and heat softening resistance [8,79], contributing to their superior high-temperature strength. RHEAs, typically characterized by significant lattice distortion and modulus mismatch, demonstrate superior strength [8,79] or super-elasticity [29] under high temperatures. For instance, in the CrMoNbV RHEA, a gigapascal compressive yield strength at 1273 K was formed due to the substantial modulus mismatch and atomic-size mismatch between Cr and other constituents [7]. In our study, we discovered that a large lattice strain was formed in our T42 HEA (refer to Fig. 4) due to

<div style="text-align: center;"><img src="imgs/img_in_chart_box_84_112_591_460.jpg" alt="Image" width="42%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_630_112_1108_457.jpg" alt="Image" width="40%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_101_458_623_812.jpg" alt="Image" width="43%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_639_459_1107_805.jpg" alt="Image" width="39%" /></div>


<div style="text-align: center;">Fig. 10. Temperature dependence on the basic physical properties of T42 alloy. a, Lattice constants as a function of temperature. b, Influence of temperature on elastic constants (C11, C12, C44) and Zener anisotropy ratio. c and d, Comparison of Young's and shear moduli between the target RHEA with pure constituents as well as CrMoNbV and Inconel 718 alloy [7].</div>


significant lattice radius mismatch but less modulus mismatch [10] than the CrMoNbV alloy [7]. This can enable superior yield strength at RT (refer to Fig. 5 a) in our LENS-fabricated T42 RHEA. Under elevated temperatures, strength softening would occur [7] and deteriorative mechanical properties would result from phase decomposition in HfNbTiZrTa alloy [12] even though the mentioned RHEA has significant lattice distortion [9]. We conducted EBSD and TEM experiments on deformed structures under different temperature conditions, revealing the presence of a single phase regardless of temperatures rather than the phase decomposition (Figs. 7 and 8) supported by the calculated phase diagram in Fig S1 (SI). Additionally, the value of lattice distortion shows a positive correlation with temperature increase [7], indicating that larger lattice distortion would be produced under elevated temperatures, enabling the stability of high yield strength in our T42 alloy under elevated temperatures.

On the other hand, the high-temperature strength can also be influenced by the temperature dependence of the elastic modulus [7], which determines the zero-temperature yield strength as well as the energy barrier for the thermal-activated flow [80,81]. In other words, the insensitive temperature dependence in the elastic constants can maintain the yield strength at elevated temperatures [7] and postpone the formation of softening. Although we did not include the lattice distortion in our first principles calculation (details given in Note 1, SI). The calculated moduli were used in the CPFEM, demonstrating significant consistency between the experimental and simulation results (Fig. 11 d). This validates the proposed methods for studying the temperature-dependence on the basic physical properties under elevated temperatures. Although a larger temperature-dependence in both E and G was observed in CrMoNbV and Inconel 718 alloys [7], the rule of mixtures on moduli [82] can also be used for calculating the modulus of materials, especially for Nb and V, with a weak temperature dependence [7,35], which were proven to maintain the high-temperature strengths in the reported alloy.



We proceeded to discuss the deformation mechanism in the deformed T42 alloy. The presence of lattice distortion led to the observation of wavy-like and pinned dislocations in the deformed alloy under room temperature (RT), as depicted in Fig. 8. This is due to the interstitial solute atoms creating a heterogeneous stress field [83], which pins the gliding dislocations and transforms the straight dislocation line into a wavy configuration [84]. At elevated temperatures, dislocation loops were also observed in samples deformed at 673 K and 873 K (see Fig. 8 b and c), facilitated by the strong solute pinning effect caused by the even larger distorted lattice [85] under these temperatures. Despite non-screw dislocations being proven effective for improving high temperature hardening in RHEAs [80,81,86], our study observed mixed characteristics of dislocations in the deformed T42 alloy at 873 K (Fig. 8 c), exhibiting a similar dislocation structure to the hot compressed CrMoNbV alloy [7].

#### 4.3. The failure mechanism of RHEA under higher temperature

The work-hardening effect present in the 673 K tensioned T42 sample makes it easier to understand that effective work-hardening delays the formation of necking [87] than in the RT-deformed sample.

<div style="text-align: center;">a</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_145_117_525_515.jpg" alt="Image" width="31%" /></div>


<div style="text-align: center;">b</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_587_143_909_504.jpg" alt="Image" width="27%" /></div>


<div style="text-align: center;">C</div>


<div style="text-align: center;">(001)</div>


<div style="text-align: center;">(011)</div>


<div style="text-align: center;">(111)</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_147_540_922_848.jpg" alt="Image" width="65%" /></div>


<div style="text-align: center;">d</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_140_902_1052_1409.jpg" alt="Image" width="76%" /></div>


<div style="text-align: center;">True stain</div>


<div style="text-align: center;">Fig. 11. a, Constructed 3D EBSD morphology. b, RVEs used in CPFEM with the similar crystal structure of experimental results. c, Assigned grain orientations in the built RVEs used for CPFEM. d, Comparison between the experimental and simulation results.</div>


<div style="text-align: center;">Table 2 Calculated AARE and R values.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>RT</td><td style='text-align: center; word-wrap: break-word;'>673 K</td><td style='text-align: center; word-wrap: break-word;'>773 K</td><td style='text-align: center; word-wrap: break-word;'>873 K</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>AARE (%)</td><td style='text-align: center; word-wrap: break-word;'>0.71</td><td style='text-align: center; word-wrap: break-word;'>0.84</td><td style='text-align: center; word-wrap: break-word;'>3.20</td><td style='text-align: center; word-wrap: break-word;'>2.64</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>R (%)</td><td style='text-align: center; word-wrap: break-word;'>99.82</td><td style='text-align: center; word-wrap: break-word;'>99.91</td><td style='text-align: center; word-wrap: break-word;'>99.18</td><td style='text-align: center; word-wrap: break-word;'>99.86</td></tr></table>

<div style="text-align: center;">Constitutive parameters obtained via CPFEM of T42 RHEA.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>Symbol</td><td style='text-align: center; word-wrap: break-word;'>Description</td><td style='text-align: center; word-wrap: break-word;'>Value</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Elastic parameters</td><td style='text-align: center; word-wrap: break-word;'>$ C_{11}, C_{12}, C_{44} $</td><td style='text-align: center; word-wrap: break-word;'>Elastic constants</td><td style='text-align: center; word-wrap: break-word;'>Via DFT</td></tr><tr><td rowspan="9">Dislocation glide parameters</td><td style='text-align: center; word-wrap: break-word;'>$ b_{s} $</td><td style='text-align: center; word-wrap: break-word;'>Burgers vector for slipping</td><td style='text-align: center; word-wrap: break-word;'>$ 2.87 \times 10^{-10} $ m</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ N_{slip} $</td><td style='text-align: center; word-wrap: break-word;'>Total number of slip systems</td><td style='text-align: center; word-wrap: break-word;'>12</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \triangle F $</td><td style='text-align: center; word-wrap: break-word;'>The activation energy for dislocation glide</td><td style='text-align: center; word-wrap: break-word;'>Changing response to temperature</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \tau_{0}^{*} $</td><td style='text-align: center; word-wrap: break-word;'>Short-range barriers strength</td><td style='text-align: center; word-wrap: break-word;'>850 MPa</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \rho_{0}^{*} $</td><td style='text-align: center; word-wrap: break-word;'>Initial dislocation density</td><td style='text-align: center; word-wrap: break-word;'>$ 6.3 \times 10^{13} $ m $ ^{-2} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>p/q</td><td style='text-align: center; word-wrap: break-word;'>Exponents in slip velocity</td><td style='text-align: center; word-wrap: break-word;'>1.0/1.15</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ v_{0} $</td><td style='text-align: center; word-wrap: break-word;'>Reference velocity for slipping</td><td style='text-align: center; word-wrap: break-word;'>$ 10^{-4} $ m/s</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ i_{s} $</td><td style='text-align: center; word-wrap: break-word;'>Parameter controlling the dislocation MFP</td><td style='text-align: center; word-wrap: break-word;'>85</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \xi_{\alpha\beta} $</td><td style='text-align: center; word-wrap: break-word;'>Interaction coefficients between slip systems</td><td style='text-align: center; word-wrap: break-word;'>0.122, 0.122, 0.625, 0.07, 0.137, 0.122</td></tr></table>

When the tensile temperature was increased to 773 K, oxidation of the base metal occurred [88], inducing surface cracks under external stress [89], and presenting regional transcrystalline fracture characteristics on the fracture surface (Fig. 6 a (iii)). Further increasing the tensile temperature resulted in a mixed fracture structure of transcrystalline with regional ductile dimples (Fig. 6 a (iv)), due to the transgranular internal oxidation [90]. At a tensile temperature of 1073 K, failure occurred even before the application of external stress. Therefore, we conducted a long-term high-temperature oxidation test, with the oxidation gain summarized in Fig. 9 c, showing a linear increase with processing time. After the high-temperature oxidation process, varieties of oxidation products were formed, which exhibit different expansion rates during the growth process. The Pilling-Bedworth ratio ( $ R_{P-B} $) of the oxidation product can be used to evaluate its cracking trend during the oxidation behavior, expressed as follows [91,92].

 $$ R_{P-B}=\frac{V_{o}}{n\bullet V_{m}}=\frac{M_{o}\bullet\rho_{m}}{n\bullet M_{m}\bullet\rho_{o}} $$ 

where M is the molecular mass,  $ \rho $ denotes the density (base metals with subscript m and oxides with subscript o), and n is the metallic atomic number in one molecule. Hence,  $ Nb_{2}O_{5} $ and  $ V_{2}O_{5} $ have  $ R_{p-B} $ values higher than 2, which are 2.665 and 3.240, respectively. This indicates that the oxidation film containing  $ N_{2}O_{5} $ and  $ V_{2}O_{5} $, with  $ R_{p-B} $ values higher than 2, is prone to expand and crack, leading to the formation of loose oxidation film after the hot temperature oxidation process [93]. As a result, surface cracks formed spontaneously (Fig. 9 a) and severe cleavage also occurred in the 120-h oxidized T42 sample (Fig S 3 in SI) during the high-temperature oxidation test, indicating the need for a stable and thick oxide layer formation element in the future [7].

## 5. Conclusions

In this study, the T42 RHEA was successfully synthesized using the LENS approach, and its microstructure, high-temperature tensile properties, lattice distortion, and high-temperature elastic constants were thoroughly investigated. The main conclusions are as follows.

1) The LENS-fabricated T42 alloy exhibited a large local lattice strain of 3.68 %, detected via the PDF approach, attributed to the presence of a large radius mismatch and local chemical fluctuations. These factors contribute to the excellent yield strength at room temperature.



2) As the temperature increases, the fabricated T42 alloy demonstrates stable yield strengths ranging from 680 to 635 MPa in the elevated temperature range. The modulus of the fabricated T42 alloy shows low sensitivity to temperature, enabling it to overcome heat softening at elevated temperatures. The effect of lattice distortion remains significant, providing considerable yield strength compared to other RHEAs under certain temperature ranges.

3) However, increasing the working temperature to 1073 K results in severe oxidation without the formation of a solid oxidation layer, leading to the complete fracture of the fabricated T42 alloy in our study. This highlights the need to consider the addition of elements that can promote the formation of solid oxidation films in future studies.

## CRediT authorship contribution statement

Yongyun Zhang: Writing – original draft, Methodology, Investigation, Formal analysis, Data curation, Conceptualization. Kaiping Yu: Methodology, Formal analysis, Data curation. Bailiang Qin: Investigation, Formal analysis. Congrui Yang: Methodology, Investigation. Shulong Ye: Writing – review & editing, Resources, Data curation, Conceptualization. Chuangshi Feng: Methodology, Formal analysis, Data curation. Fuxiang Zhang: Resources, Investigation, Funding acquisition. Di Ouyang: Methodology, Investigation, Formal analysis. Lin Liu: Writing – review & editing, Project administration, Funding acquisition. Haibo Ke: Writing – review & editing, Project administration, Funding acquisition. K.C. Chan: Writing – review & editing, Software, Resources, Project administration, Funding acquisition. Wei-hua Wang: Writing – review & editing, Supervision, Resources, Project administration, Funding acquisition.