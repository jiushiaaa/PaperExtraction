Research Article

# An additively manufactured precipitation hardening medium entropy alloy with excellent strength-ductility synergy over a wide temperature range

<div style="text-align: center;"><img src="imgs/img_in_image_box_997_336_1055_391.jpg" alt="Image" width="4%" /></div>


Jing Huang $ ^{a,b} $, Wanpeng Li $ ^{b,c,*} $, Tao Yang $ ^{b} $, Tzu-Hsiu Chou $ ^{b} $, Rui Zhou $ ^{b} $, Bin Liu $ ^{a} $, Jacob C. Huang $ ^{b,d,*} $, Yong Liu $ ^{a,*} $

 $ ^{a} $State Key Laboratory of Powder Metallurgy, Central South University, Changsha 410083, China

 $ ^{b} $ Department of Materials Science and Engineering, City University of Hong Kong, Kowloon 999077, Hong Kong SAR, China

 $ ^{c} $TRACE EM Unit, City University of Hong Kong, Kowloon 999077, Hong Kong SAR, China

 $ ^{a} $Department of Materials and Optoelectronic Science, National Sun Yat-Sen University, Kaohsiung 804, Taiwan, China

#### ARTICLE INFO

Article history:

Received 6 October 2023

Revised 12 January 2024

Accepted 28 February 2024

Available online 9 April 2024

Keywords:

Additive manufacturing

Selective laser melting

Medium entropy alloy

Multi-principal-element alloy

Precipitation hardening

Mechanical properties

## A B S T R A C T

Modern engineering has long been in demand for high-performance additive manufactured materials for harsh working conditions. The idea of high entropy alloy (HEA), medium entropy alloy (MEA), and multi-principal-element alloy (MPEA) provides a new way for alloy design. In this work, we develop a  $ Co_{42}Cr_{20}Ni_{30}Ti_{4}Al_{4} $ quinary MEA which exhibits a superiority of mechanical properties over a wide temperature ranging from 77 to 873 K via selective laser melting (SLM) and post-heat treatment. The present MEA achieves an excellent ultimate tensile strength (UTS) of 1586 MPa with a total elongation (TE) of 22.7 % at 298 K, a UTS of 1944 MPa with a TE of 22.6 % at 77 K, and a UTS of 1147 MPa with a TE of 9.1 % at 873 K. The excellent mechanical properties stem from the microstructures composed of partially refined grains and heterogeneously precipitated  $ L_{12} $ phase due to the concurrence of recrystallization and precipitation. The grain boundary hardening, precipitation hardening, and dislocation hardening contribute to the high YS at 298 and 77 K. Interactions of nano-spaced stacking faults (SFs) including SFs networks, Lomer–Cottrell locks (L–C locks), and anti-phase boundaries (APBs) induced by the shearing of  $ L_{12} $ phase are responsible for the high strain hardening rate and plasticity at 77 K. Our work provides a new insight for the incorporation of precipitation hardening and additive manufacturing technology, paving the avenue for the development of high-performance structural materials.

© 2024 Published by Elsevier Ltd on behalf of The editorial office of Journal of Materials Science & Technology.

### 1. Introduction

High-performance alloys with gigapascal strength and good ductility are highly desired for modern engineering applications. The idea of high entropy alloy (HEA), medium entropy alloy (MEA), and multi-principal element alloy (MPEA) provides a new avenue for the further extension of the up-limit of strength-ductility combination in the face-centered cubic (FCC) metal materials [1,2]. The high work-hardening capability but relatively low strength of the face-centered-cubic (FCC) MPEAs [2], which are mainly composed of Fe, Co, Cr, Ni, and Mn, makes it a quite hot topic to strengthen them. As an effective and widely used strengthening method, precipitation hardening has also been adopted into the FCC MPEAs, among which the L12 phase strengthened MPEAs exhibit superior mechanical properties [3–9]. The coherent interface between the L12 phase and the FCC matrix could effectively reduce the stress concentration and avoid the premature failure of the alloy [10–12]. The L12 precipitates introduced via the co-doping of Ti and Al exhibit lower environmental embrittlement, which achieves a less loss of ductility in the intermetallic phase strengthened alloys [4]. Moreover, the small interfacial energy of the L12/FCC interface and the slower diffusion effect of HEA contribute to the thermal stability of the L12 phase [13], and the L12 solvus temperature can be raised to 1150 °C with appropriate alloying optimization [14], making the L12 phase a promising strengthening phase at elevated temperatures.



The equiatomic CoCrNi system exhibits excellent work-hardening ability, and a more prominent combination of strength and ductility compared with other CoCrFeMnNi HEAs at room temperature and especially the cryogenic temperature  $ [2,15] $.

making the CoCrNi MEA an ideal FCC matrix for the precipitation strengthening. The exceptional mechanical properties of CoCrNi MEA are attributed to twinning-induced plasticity (TWIP) and transformation-induced plasticity (TRIP), which are widely admitted to be closely related to stacking fault energy (SFE) [16]. In recent years, studies about the non-equiatomic CoCrNi MEAs reveal that tuning the content of Co can regulate the SFE of the alloy and achieve higher work-hardening ability, making the further optimization of mechanical properties of CoCrNi MEAs a promising project [16,17]. For Ti/Al containing CoCrNi-based MEAs, a lower content of Cr is also reported to be effective in reducing the formation of the detrimental  $ \sigma $ phase, indicating the composition design is of substantial importance in the optimization of precipitation-strengthened CoCrNi-based MEAs [6].

However, the fabrication of casting alloys mentioned above mostly involves multiple passes of mechanical treatments and heat treatments to attain a tailored microstructure, making the production routes laborious work, especially for the complex geometries. Compared with the conventional fabrication routes, additive manufacturing (AM) exhibits several superiorities, such as a high degree of geometrical freedom in the design and production of metal components with complex structures, a substantial reduction in the loss of raw materials during post-processing compared to the conventional fabrication method, and the consequent time, energy, and cost-saving [18–21]. Moreover, the high energy input and high cooling rate of AM methods can suppress phase transition and intermetallic formation, and also lead to a fine microstructure, making it a potential fabrication route for MPEAs.

As one of the most prominent AM techniques, selective laser melting (SLM) is widely applied to research about HEAs. The research about the selective laser melted (SLMed) equiatomic FeCoCrNiMn-based HEAs indicated that the fine grain structures, cellular structures, and dislocations brought by SLM methods do favor the improvement on the strength of HEAs compared to the counterparts produced by casting [22–24]. The high cooling rate of SLM also facilitates the formation of the single FCC structure and the introduction of solid solution hardening brought by the substitutional and interstitial solute atoms. Park et al. [25] reported a simultaneous improvement in the strength and ductility of FeCoCrNiMn SLMed HEA by introducing 1 % C. Fujieda et al. [26] attributed the decent synergy of strength-ductility (tensile strength of 1178.0 MPa and elongation of 25.8 %) and the improved corrosion resistance of the Co₁.₅CrFeNi₁.₅Ti₀.₅Mo₀.₁ alloy to fine grain structures and the absence of Ni₃Ti intermetallic compounds. In addition to the solid solution hardening effect, introducing interstitial atoms, such as nitrogen, can lead to further strain hardening mechanisms in SLMed HEAs. Song et al. [27] reported that the nitrogen doping induced a local grain refinement in the re-melted regions during SLM, and the subsequent heterogeneous deformation induced hardening. For the eutectic HEA, the lamellar eutectic structure can be refined via the application of SLM. Yang et al. [28] reported a SLMed Ni₃Co₀Cr₁₀Fe₁₀Al₁₈W₁Mo₁ (at.%) with an ultra-fine lamellar spacing of 150–200 nm within the small colony with the size of 2–6 μm, exhibiting a yield strength of 1.0 GPa, ultimate tensile strength of 1.4 GPa, and uniform elongation larger than 18 %. Introducing nano secondary particles is also feasible in SLMed HEAs. Lu et al. [29] produced a FeCoCrNiMn-TiC HEA composite via SLM, which exhibits both an increase in strength and ductility compared to the FeCoCrNiMn HEA.

Moreover, with a tailored composition and post-heat treatments, nano precipitates, such as the L1₂ phase mentioned above, can also be introduced into the SLMed HEAs, leading to a further improvement in the mechanical properties with the combination of precipitation hardening and advantages of the SLM method. The (CoCrNi)₉₄Ti₃Al₃ alloy reported by Yao et al. [30] benefits from the low stacking faults energy (SFE) of the matrix, the hierarchical microstructure composed of precipitation and heterogeneous grain structure, and the inherent high density of dislocations, exhibiting superior mechanical properties at cryogenic and ambient temperature. The SLMed (FeCoNi)₈₆Ti₇Al₇ alloy reported by Mu et al. [31] exhibits a unique dislocation-precipitate skeleton (DPS), ultrahigh ultimate tensile strength of ~1.8 GPa, and maximum elongation of ~16 % at the ambient temperature. However, it meets a bottleneck to raise the volume fraction of L1₂ precipitates with the equiatomic CoCrNi matrix, since higher Ti/Al contents bring about the precipitation of σ phase that deteriorates mechanical properties [32–34]. The equiatomic FeCoNi matrix shows a large solid solubility of Al and Ti, but the inevitable L2₁ phase (Ni₂TiAl) is harmful to the mechanical performance at elevated temperatures [31,35,36]. Hence, increasing the volume fraction of L1₂ precipitates and avoiding the formation of detrimental phases are striving goals for the alloy design of L1₂-strengthened AMed MPEAs. Meanwhile, modern engineering has put forward more urgent requests for structural materials with excellent mechanical properties at harsh working conditions [21], such as at cryogenic or elevated temperatures, making the development of high-performance AMed alloys a challenging but promising subject.



In this study, a non-equiatomic  $ Co_{42}Cr_{20}Ni_{30}Ti_{4}Al_{4} $ quinary MEA was developed via SLM plus the post-heat treatment, exhibiting superior mechanical properties over a wide temperature range (from 77 to 873 K). A high volume fraction of heterogeneously precipitated  $ Li_{2} $ precipitates and the partially recrystallized FCC matrix were introduced into the MEA simultaneously without other harmful phases. The strengthening and deformation mechanisms were investigated and discussed based on the microstructural observation. Our work provides insights into the development of AMed  $ Li_{2} $ strengthened alloys, and also indicates that, with the combination of proper elemental designs and heat treatments, additive manufacturing could be a promising processing technique for high-performance structural materials.

### 2. Materials and methods

#### 2.1. Alloy design

The nominal composition of the alloy and heat treatment processes were designed according to previous studies and experiments. Firstly, higher contents of Ni (30 at.%), Ti (4 at.%), and Al (4 at.%) were chosen for introducing a high volume fraction of the L1₂ phase with high anti-phase boundary (APB) energy [37]. Although even higher contents of Ti and Al were verified to be practical and effective in strengthening the alloy, it is possible to bring about the B2 phase and L2 phase [35,38]. Relatively lower Cr was preferred to avoid the introduction of the σ phase [33,34]. High content of Co was preferred to lower the SFE, which may endow the alloy with better sustainability of a high strain-hardening rate at higher strain conditions [39,40]. The pseudo-binary equilibrium phase diagram with varying Cr content was calculated by the Thermo-Calc software (TCHEA5 database), as shown in Fig. S1 in Supplementary Information. Fig. S1 indicates that 42 at.% of Co and 20 at.% of Cr can effectively avoid the possible detrimental σ phase. Therefore, the composition of the alloy was determined to be Co4₄Cr₂₀Ni₃₀Ti₄Al₄ (at.%).

The configuration entropy of the Co₄₂Cr₂₀Ni₃₀Ti₄Al₄ (at.%) alloy was calculated to be 1.3R (The calculation method is shown in Section 2 in Supplementary Information). It meets the definition of MEAs [41]: 1.0R ≤ ΔS_conf ≤ 1.5R, when the alloy is in a random solution state. Therefore, the Co₄₂Cr₂₀Ni₃₀Ti₄Al₄ (at.%) alloy is referred to as an MEA.

The suitable parameters for the heat treatments were chosen via the combination of annealing trials, hardness tests, and microstructural characterizations. All the trials were attempted in

<div style="text-align: center;">a</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_140_119_543_503.jpg" alt="Image" width="33%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_551_121_1051_495.jpg" alt="Image" width="41%" /></div>


<div style="text-align: center;">(c)</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_138_535_552_875.jpg" alt="Image" width="34%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_569_529_1014_890.jpg" alt="Image" width="37%" /></div>


<div style="text-align: center;">Fig. 1. (a) The morphology of the pre-alloyed powder. (b) The particle size distribution map of the pre-alloyed powder. (c) Schematic drawing of the SLM process. And (d) the XRD patterns of the as-built and as-annealed alloys.</div>


SLMed samples. The results indicated that annealing at 973 K for 64 h was the optimum heat treatment condition.

### 2.2. Materials fabrication

Pre-alloyed Co₄₂Cr₂₀Ni₃₀Ti₄Al₄ (at.%) powders were produced by gas atomization, exhibiting spherical shape and FCC structure as shown in Fig. 1(a). The particle size ranged from 8 to 60 μm with an average diameter of 22.9 μm (Fig. 1(b)). The SLM process was conducted on a sandblasted stainless-steel substrate using a commercial machine (FS121M-B5, Farsoon, China), with a laser power of 200 W, scanning speed of 1000 mm s⁻¹, hatching space of 90 μm, beam size of 40 μm and the layer thickness of 40 μm. Argon atmosphere was used to prevent oxidation during SLM. The laser was rotated 67° in each scanning layer as shown in Fig. 1(c). The geometry of the as-built material block was in a cuboid shape, with a length of 65 mm, width of 18 mm, and height of 10 mm. The as-built material blocks together with the substrate were annealed at 723 K for 3 h followed by water quenching to release the residual stress. After the residual stress relief heat treatment, the as-built blocks were removed from the substrate by wire-electrode cutting, then annealed at 973 K for 64 h followed by water quenching. The as-built blocks that went through the residual stress relief heat treatment are referred to as the as-built alloy, and the blocks that went through two passes of heat treatments are referred to as the as-annealed alloy.



### 2.3. Mechanical testing

The specimens for tensile tests were prepared via slicing the as-built blocks by wire-electrode cutting. The uniaxial tensile tests at room temperature (298 K) were conducted on the Instron 3369 machine equipped with an extensometer, using flat dog-bone-shaped specimens with a gage length of 20 mm, and width of 4 mm. The uniaxial tensile tests at 77 K were conducted on an MTS Alliance RT 30 tensile machine, using flat dog-bone-shaped specimens with a gage length of 12.5 mm, and width of 3 mm. The uniaxial tensile tests at 773 and 873 K were conducted on an RRC-50 testing machine, using flat dog-bone-shaped specimens with a gage length of 8 mm, and a width of 3.4 mm. Each sample has a thickness of  $ \sim $1.5 mm after polishing. A strain rate of  $ 1 \times 10^{-3} $ s $ ^{-1} $ was applied to all the tensile tests. Each test condition was repeated at least three times to ensure the reproducibility. In particular, before starting a tensile test at 77 K, the specimen was held at 77 K for 5 min. Before starting a tensile test at 773 and 873 K, the specimen was held at the testing temperature for 10 min.

#### 2.4. Microstructural characterization

The particle size distribution of the pre-alloyed powders was estimated by using a laser diffraction particle size analyzer (Malvern, Micro-plus). The porosity of the as-built alloy was measured by the metallographic methods. The densities of the as-built alloy and the casting alloy with the same composition were measured by the Archimedes method. Each density data was measured three times to ensure accuracy. The crystal structure and phase composition of pre-alloyed powders, the as-built alloy, and the as-annealed alloy were characterized by X-ray diffraction (XRD, Rigaku D/MAX-2250, Japan) with Cu Kα radiation. The bulk samples for XRD characterization were polished using standard mechanical polishing procedures. The scanning step for all the XRD measurements is 0.02°. The scanning in the 2θ range of 20°–100° was conducted with a scanning speed of 5° min⁻¹. A slow scan in the 2θ range of 20°–37° was conducted with a scanning speed of 0.5° min⁻¹. The micromorphology of pre-alloyed powders, the overview of the microstructures, and fracture surfaces were conducted on the scanning electron microscopy (SEM, TESCAN MIRA4 LMH) equipped with an energy dispersive spectrometer (EDS, Ultim Max 40) and electron backscatter diffraction (EBSD) detector. The specimen sheets for SEM and EBSD analysis were firstly mechanically ground to 3000-grit SiC paper, followed by mechanical polishing by colloidal silica suspension, and finally electrochemically polished by 10 % HClO₄ + 90 % C₂H₅OH solution at 233 K and 25 V. The EBSD data were analyzed by the Aztec Crystal software. TEM characterizations were performed by transmission electron microscope (TEM, JEOL JEM-2100F, and JEM-ARM300F2, Japan) equipped with an energy dispersive spectrometer (EDS). STEM (scanning transmission electron microscopy) images were taken using an annular-type detector with a collection angle ranging from 92 to 228 mrad. The corresponding EDS mapping was collected and processed by the auto filter in the Oxford INCA software. TEM samples were sliced by wire-electrode cutting, and then mechanically ground to about 50 μm by SiC paper, and finally twin-jet electro-polished in 10 % HClO₄ + 90 % C₂H₅OH solution at 243 K and 25 V.

### 3. Results

#### 3.1. As-built and as-annealed microstructures

The porosity value of the as-built alloy was measured to be 0.048 % via metallographic methods. The porosity value is the average value of the area ratios of porosities in the metallographs shown in Fig. S2. The areas were measured by Image J. The density of the as-built alloy is  $ 8.07 \pm 0.02 $ g  $ mm^{-3} $, and the density of the corresponding casting alloy is  $ 8.13 \pm 0.02 $ g  $ mm^{-3} $. Therefore, the relative density is calculated to be 99.26 %, indicating that the as-built alloy is nearly fully dense. The XRD patterns in Fig. 1(d) indicate that the FCC phase is present in the as-built and as-annealed alloys, while the L12 precipitate phase is introduced during the annealing process. Fig. 2 shows the comparison of the grain structures before and after the annealing. The as-built alloy exhibits clear melting tracks (Fig. 2(a)) and typical columnar grains (Fig. 2(b)). After annealing, a large number of fine grains emerge as shown in Fig. 2(c, d), indicating that recrystallization happens. Given the morphology of grains in the as-annealed alloy, the recrystallization has only partially proceeded [42,43]. The decreasing grain reference orientation deviation (GROD) in the as-annealed alloy, which is shown by the comparison between Fig. 2(e, f) and Fig. 2(g, h), confirms the occurrence of recrystallization. Correspondingly, the newly formed fine recrystallized grains lead to a decreasing average grain size and a decrease in the density of geometrically necessary dislocations (GNDs) which is reflected by the decreasing values of Kernel average misorientation (KAM). The corresponding KAM distribution maps and grain size distribution maps are shown in Fig. S3.



Fig. 3 illustrates the detailed microstructures of the alloy before and after the annealing treatment. As shown in Fig. 3(a), the grains in the as-built alloy are composed of uniform sub-grain cellular structures, and no precipitates occur. The cellular structures are columnar structures that are displayed cross-sectionally.

After the annealing, the cellular structures become coarsened. The average diameter of cellular structures in the as-built alloy and the as-annealed alloy is measured to be 0.63 and 1.24  $ \mu $m, respectively. The non-uniform growth of discontinuous precipitation (DP) colonies is prevalently around grain boundaries, which is indicated by arrows in Fig. 3(b). Discontinuous precipitates exhibit typical lamellar or short-rod shape. At higher magnification, it can be observed that the DP not only happens at regions near grain boundaries but can also proceed deeply into the grains as presented in Fig. 3(c). Discontinuous precipitates distributed more inside the grain exhibit finer and shorter rod shapes, some even near-spherical. Moreover, DP is also evidently observed in the newly formed fine recrystallized grains where the cellular structures vanish (Fig. 3(d)) and some annealing twins form (Fig. 3(e)). However, no visible precipitate is observed in the regions typically shown in Fig. 3(f) where cellular structures are undamaged.

To further investigate the microstructures, TEM characterization was conducted. Fig. 4(a) shows the distinct cellular structures with sizes around 0.5–1  $ \mu $m in the as-built alloy. The inserted selected-area electron diffraction (SAED) pattern indicates that the as-built alloy has a single FCC structure. The two-beam bright-field (BF) image (Fig. 4(b)) and low-angle annular dark-field (LAADF) scanning transmission microscopy (STEM) image (Fig. 4(c)) reveal that the cellular boundaries are composed of dislocation walls. In addition to the dislocation walls, there are also many dislocations inside the cellular structures. The corresponding STEM energy-dispersive X-ray spectroscopy (EDS) results show the Ti segregation on the cellular boundaries.

The TEM BF image (Fig. 5(a)) and the corresponding dark-field (DF) image (Fig. 5(b)) distinctly show the strip-like morphology of discontinuous precipitates. The inserted SAED pattern confirms that the matrix has FCC structure and the discontinuous precipitates have the L1₂ structure. The two-beam BF image (Fig. 5(c)) shows a relatively larger view of the DP region. The tangled dislocations that make up the cell boundaries are mostly annihilated, and only some traces of remaining dislocations walls can still be identified as referred to by arrows in Fig. 5(c). The high-angle annular dark-field (HAADF) image (Fig. 5(d)) also shows that the original cellular boundaries composed of tangled dislocations are eliminated, but the distribution of precipitates in the DP region exhibits a cellular contour. The corresponding STEM-EDS results (Fig. 5(e)) show obvious segregation of Ni, Ti, and Al along cellular contours. Fig. 6 gives the HAADF-STEM image and the corresponding EDS mapping of discontinuous L1₂ precipitates with higher magnification. The concentration of Ni, Ti, and Al inside the cellular contour exhibits a stripe-like shape, which corresponds to the morphology of discontinuous L1₂ precipitates. Meanwhile, the HAADF-STEM image shows that there are more L1₂ precipitates along the cellular contour, indicating that more L1₂ precipitates form along the original cellular boundaries where there was a segregation of Ti, and they subsequently make up of the cellular contour with no dislocations. But in the areas near grain boundaries, where discontinuous precipitates show larger sizes, cellular contours with enrichment of Ni, Ti, and Al are eliminated as shown in Fig. S4.

In addition to the DP region with annihilated dislocation walls, the undamaged cellular structures can be observed in the as-annealed alloy as Fig. 7(a) shows. The inserted SAED pattern

<div style="text-align: center;"><img src="imgs/img_in_image_box_231_116_959_641.jpg" alt="Image" width="61%" /></div>


<div style="text-align: center;">Fig. 2. EBSD results of the microstructures for the as-built and as-annealed alloys (step size = 0.2 μm). The inverse pole figure (IPF) maps (a–d), Grain Reference Orientation Deviation (GROD) maps (e–h) of the XY plane (a, e) for the as-built alloy, the XZ plane (b, f) for the as-built alloy, the XY plane (c, g) for the as-annealed alloy, and the XZ plane (d, h) for the as-annealed alloy, respectively.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_259_736_930_1181.jpg" alt="Image" width="56%" /></div>


<div style="text-align: center;">Fig. 3. BSE (back scatter electron) observations of the microstructures on the XY plane for the as-built and as-annealed alloys. (a) The as-built alloy showing uniform cellular structures. (b) The as-annealed alloy showing DP around grain boundaries. (c) An enlarged view of the inside region of the grains in the as-annealed alloy showing fine discontinuous precipitates. (d) DP in the newly formed recrystallized grain in the as-annealed alloy. (e) DP in the annealing twins in the as-annealed alloy. (f) Regions with undamaged cellular structures but no visible precipitates in the as-annealed alloy.</div>


(Fig. 7(a)) and the DF image (Fig. 7(b)), which corresponds to the area labelled with the red dash-lined rectangle in Fig. 7(a), indicate the continuous precipitation (CP) of L1₂ precipitates. The continuous L1₂ precipitates are spherical, and much smaller than the discontinuous L1₂ precipitates so they can only be characterized via TEM. Hence, there is no visible precipitate in Fig. 3(f). The LAADF-STEM image of the CP region (Fig. 7(c)) shows that cellular boundaries composed of dislocation walls are still maintained after the CP happens. The corresponding STEM-EDS results (Fig. 7(d)) also shows an obvious enrichment of Ni, Ti, and Al along cell boundaries. The LAADF-STEM image with higher magnification of the region inside the cellular structure, where marked with a dash-lined square in Fig. 7(c), and its corresponding STEM-EDS results (Fig. 7(e)) confirm the presence of continuous L1₂ precipitates inside the cellular structure. The enlarged view of the dislocation wall, where marked with a dash-lined circle in Fig. 7(c), and the corresponding STEM-EDS results (Fig. 7(f)) confirm that there are also L1₂ precipitates within the dislocation wall. Compared



<div style="text-align: center;"><img src="imgs/img_in_image_box_235_115_954_831.jpg" alt="Image" width="60%" /></div>


<div style="text-align: center;">Fig. 4. TEM observations of the as-built alloy. (a) TEM BF image of the as-built microstructure showing cellular structures. (b) TEM two-beam BF image showing cell boundaries composed of dislocations. (c) LAADF-STEM image and the corresponding STEM-EDS maps of cellular structures in the as-built alloy.</div>


with the intra-cellular precipitates, the inter-cellular precipitates exhibit a more ellipsoidal shape. Similar dislocation-precipitation skeletons were also observed in the AMed Fe $ _{28} $Co $ _{29.5} $Ni $ _{27.5} $Ti $ _{8.5} $Al $ _{6.5} $ alloy [31], and the morphology difference between intra-cellular precipitates and the inter-cellular precipitates was ascribed to the pipe-diffusion mechanism and the elemental dragging effect. The atomic-scale high-resolution (HR) TEM observation in Fig. 8 shows that both the discontinuous precipitates and continuous precipitates are fully coherent with the FCC matrix. The corresponding fast Fourier transform (FFT) patterns further confirm the L12 structure of precipitates.

The representative engineering stress-strain curves of the as-built alloy tested at 298 and 77 K, and the as-annealed alloy at 298, 77, 773, and 873 K are presented in Fig. 9(a). The values of yield strength (YS), ultimate tensile strength (UTS), and total elongation (TE) are listed in Table 1. Compared to the results at 298 K, the as-built alloy shows an increase in both strength and ductility at 77 K.

#### 3.2. Mechanical properties at different temperatures

After annealing, the alloy at 298 K exhibits a great improvement for the YS (734 ± 9 to 1180 ± 10 MPa) and UTS (995 ± 7 to 1586 ± 11 MPa) and still maintains excellent ductility (22.7 % ± 0.3 %). When the testing temperature decreases to 77 K, the YS and UTS increase to 1341 ± 17 and 1944 ± 6 MPa, respectively. Meanwhile, the ductility is unaffected. At elevated tempera-

<div style="text-align: center;">Table 1 Mechanical properties of the as-built alloy and as-annealed alloy.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Alloys</td><td style='text-align: center; word-wrap: break-word;'>Test temperatures (K)</td><td style='text-align: center; word-wrap: break-word;'>YS (MPa)</td><td style='text-align: center; word-wrap: break-word;'>UTS (MPa)</td><td style='text-align: center; word-wrap: break-word;'>TE (%)</td></tr><tr><td rowspan="2">As-built</td><td style='text-align: center; word-wrap: break-word;'>77</td><td style='text-align: center; word-wrap: break-word;'>953  $ \pm $ 4</td><td style='text-align: center; word-wrap: break-word;'>1370  $ \pm $ 14</td><td style='text-align: center; word-wrap: break-word;'>49.9  $ \pm $ 2.5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>298</td><td style='text-align: center; word-wrap: break-word;'>734  $ \pm $ 9</td><td style='text-align: center; word-wrap: break-word;'>995  $ \pm $ 7</td><td style='text-align: center; word-wrap: break-word;'>37.7  $ \pm $ 1.0</td></tr><tr><td rowspan="4">As-annealed</td><td style='text-align: center; word-wrap: break-word;'>77</td><td style='text-align: center; word-wrap: break-word;'>1341  $ \pm $ 17</td><td style='text-align: center; word-wrap: break-word;'>1944  $ \pm $ 6</td><td style='text-align: center; word-wrap: break-word;'>22.6  $ \pm $ 2.9</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>298</td><td style='text-align: center; word-wrap: break-word;'>1180  $ \pm $ 10</td><td style='text-align: center; word-wrap: break-word;'>1586  $ \pm $ 11</td><td style='text-align: center; word-wrap: break-word;'>22.7  $ \pm $ 0.3</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>773</td><td style='text-align: center; word-wrap: break-word;'>977  $ \pm $ 3</td><td style='text-align: center; word-wrap: break-word;'>1263  $ \pm $ 10</td><td style='text-align: center; word-wrap: break-word;'>13.8  $ \pm $ 1.4</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>873</td><td style='text-align: center; word-wrap: break-word;'>926  $ \pm $ 11</td><td style='text-align: center; word-wrap: break-word;'>1147  $ \pm $ 16</td><td style='text-align: center; word-wrap: break-word;'>9.1  $ \pm $ 0.6</td></tr></table>

tures, the as-annealed alloy maintains high UTS of  $ 1263 \pm 10 $ and  $ 1147 \pm 16 $ MPa at 773 and 873 K, with decent ductility of  $ 13.8 \pm 1.4\% $ and  $ 9.1 \pm 0.6\% $, respectively.

The true stress-true strain curves and the corresponding strain-hardening rate curves of the as-built alloys and as-annealed alloys tested at different temperatures are shown in Fig. 9(b). For the same alloy, the strain-hardening rate at 77 K is the highest, showing an apparent temperature dependence. Meanwhile, compared to the as-built alloy, the as-annealed alloy shows a distinctly higher strain-hardening rate at the same temperature. Fig. 9(c-f) presents the comparisons of mechanical properties between the as-annealed alloy and some other AMed alloys, including MPEAs [22–24,30,31,35], MPEA/TiC composite materials [29], eutectic alloys [28], Inconel 718 alloy [44–47], Alloy 625 [48], 316 L steel [49–51], and AISI 4140 steel [52]. As shown in Fig. 9(c), although

<div style="text-align: center;"><img src="imgs/img_in_image_box_237_116_953_648.jpg" alt="Image" width="60%" /></div>


<div style="text-align: center;">rig. 3. IEM and SIEM observations of the DP region in the as-annealed alloy. (a) TEM BF image of DP region and the corresponding SAED pattern. (b) TEM DF image corresponding to (a) showing the morphology of discontinuous L1₂ precipitates. (c) TEM two-beam BF image of the DP region showing traces of annihilated cell boundaries. (d) HAADF-STEM image of the DP region showing the morphology and distribution of discontinuous L1₂ precipitates. (e) STEM-EDS results corresponding to (d) showing the enrichment of Ni, Ti, and Al along the cellular contour.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_214_763_978_1265.jpg" alt="Image" width="64%" /></div>


<div style="text-align: center;">Fig. 6. HAADF-STEM image and the corresponding STEM-EDS mapping of the DP region with higher magnification.</div>


the total elongation of the as-annealed alloy is comparable with other alloys, the ultimate tensile strength is prominently higher at 77 K. The comparison of yield strengths and total elongations shows a similar trend in Fig. S5(a). For mechanical properties at 298 K shown in Figs. 9(d) and S5(b), the as-annealed alloy exhibits a better strength-ductility combination than the alloy which exhibits the highest strengths. For the mechanical properties at elevated temperatures shown in Fig. 9(e, f), the as-annealed alloy exhibits higher strength. In general, the as-annealed alloy presented in our current work exhibits excellent mechanical properties over a wide range of temperatures from 77 to 873 K, especially the prominent mechanical properties at 77 K.



<div style="text-align: center;"><img src="imgs/img_in_image_box_186_114_1005_517.jpg" alt="Image" width="68%" /></div>


<div style="text-align: center;">Fig. 1. IEM and STEM observations of the CP region in the as-annealed alloy. (a) TEM two-beam BF image of the CP region in the as-annealed alloy showing the intact cellular boundaries composed of dislocations. (b) TEM DF image corresponding to the red dash lined rectangle in (a) showing the morphology and distribution of continuous L12 precipitates. (c) LAADF-STEM image of the CP region showing the intact cellular boundaries composed of dislocations. (d) STEM-EDS corresponding to (c) showing the enrichment of Ni, Ti, and Al along cellular boundaries. (e) STEM image and STEM-EDS results of the intra-cellular region, indicated by the square in (c). (f) STEM image and STEM-EDS results of the inter-cellular region, indicated by the circle in (c).</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_234_643_955_1173.jpg" alt="Image" width="60%" /></div>


<div style="text-align: center;">Fig. 8. (a) HR-TEM image of the discontinuous precipitate with the FFT patterns corresponding to regions labelled with numbers 1 and 2. (b) HR-TEM image of the continuous precipitate with the FFT patterns corresponding to regions labelled with numbers 3 and 4.</div>


### 3.3. Deformation substructures

To understand the deformation mechanism underlying the excellent mechanical properties of the as-annealed alloy, TEM observations on the deformed microstructure of the as-built alloy and the as-annealed alloy were conducted.

The microstructure of the as-built alloy after the deformation at 298 and 77 K is shown in Fig. 10. Compared with the microstructure before the deformation shown in Fig. 4(a, b), the density of dislocations inside cellular structures distinctly increases as Fig. 10(a) shows, suggesting a massive dislocation multiplication during the plastic deformation. The thickened cell boundaries indicate that more dislocations tangled here after the deformation, which suggests that the cell boundaries play a critical role in impeding the motion of dislocations. Similar microstructures that can hinder the movement of dislocations always play a positive effect on the strength, such as grain boundaries and interfaces between phases [53]. As shown in Fig. 10(b), the planar dislocation configuration is composed of slip bands along {111} planes while no deformation twin (DT) and stacking faults (SFs) are observed in the as-built alloy deformed at 298 K, indicating that planar dislocation glide is the main deformation mechanism. While



<div style="text-align: center;"><img src="imgs/img_in_chart_box_143_126_439_352.jpg" alt="Image" width="24%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_440_125_779_352.jpg" alt="Image" width="28%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_145_371_438_604.jpg" alt="Image" width="24%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_448_372_1048_602.jpg" alt="Image" width="50%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_140_609_445_839.jpg" alt="Image" width="25%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_445_607_903_834.jpg" alt="Image" width="38%" /></div>


<div style="text-align: center;">Fig. 3. mecanical properties of the AMed  $ \text{Co}_{42}\text{Cr}_{20}\text{Ni}_{30}\text{Ti}_{4}\text{Al}_{4} $ alloy. (a) Representative tensile engineering stress-strain curves for the present alloy tested at 77, 298, 773, and 873 K, respectively. (b) True stress-true strain curves and corresponding strain-hardening rate curves at 77, 298, 773, and 873 K, respectively; the solid lines are true stress-true strain curves, and the dots represent the strain-hardening rate. The mechanical properties of the current as-annealed alloy and some reported AMed alloys tested at (c) cryogenic temperature, (d) room temperature, and (e, f) elevated temperatures are compared.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_259_961_592_1182.jpg" alt="Image" width="27%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_598_961_930_1181.jpg" alt="Image" width="27%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_260_1187_595_1408.jpg" alt="Image" width="28%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_598_1190_931_1409.jpg" alt="Image" width="27%" /></div>


<div style="text-align: center;">Fig. 10. TEM observations of the microstructures of the as-built alloy after the deformation at (a, b) 298 K and (c, d) 77 K: (a) Two-beam BF TEM image showing the thickened cell boundaries and cell interiors with a high density of dislocations; (b) two-beam BF TEM image exhibiting the planar dislocation configuration composed of slip bands along  $ \{11\} $ planes; (c) two-beam BF TEM image showing SFs on the  $ \{11\} $ planes; (d) DF TEM image of DTs and the corresponding SAED patterns (the inset).</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_259_114_930_789.jpg" alt="Image" width="56%" /></div>


<div style="text-align: center;">Fig. 11. Typical deformation substructures in the (a) CP region and (b) DP region of the as-annealed alloy deformed at 298 K, (c, d) the CP region, and (e, f) the DP region of the as-annealed alloy deformed at 77 K; (a) two-beam BF TEM image of the intersecting SFs; (b) two-beam BF TEM image of the SFs extending in one direction; (c) BF TEM image (left) of the intersecting slip bands and the corresponding DF TEM image (right); (d) the HR-TEM image of the L12 precipitate sheared by the SF and the subsequently formed APB with an enlarged view (the inset); (e) two-beam BF TEM image of the intersecting SFs and the SF network; (f) the HR-TEM image exhibiting an L-C lock generated by two intersected SFs.</div>


at 77 K, a large number of SFs and DTs are observed in the as-built alloy after deformation, as illustrated in Fig. 10(c, d). A similar phenomenon has been observed in the other CoCrNi-based MPEA [30,54–56]. The activation of SFs and DTs could effectively relieve the stress concentration, and the newly formed SFs and DTs could further impede the motion of dislocations, thus both the ductility and strength of the as-built alloy are improved at 77 K. The tendency of activating SFs and DTs at cryogenic temperatures is ascribed to the SFE which decreases with decreasing temperature.

Fig. 11 shows the microstructure of the as-annealed alloy after deformation at 298 and 77 K. Generally, planar dislocation glide is the main deformation mechanism. At 298 K, SFs can be activated in two {111} planes in the CP regions, intersecting with each other severely, as the arrows indicated in Fig. 11(a). But in DP regions, more SFs extend in one direction (Fig. 11(b)). A similar phenomenon has been reported by Zhao et al. [54], and it is ascribed to the difference in precipitate morphology between CP and DP regions. At 77 K, a high density of intersecting slip bands shown in Fig. 11(c) indicates the severe deformation dominated by the planar glide at the CP region. Fig. 11(d) presents the L1₂ precipitate sheared by SF, forming an APB. While at the DP region, SFs are also activated in two {111} planes, and the intersection between SFs is significantly enhanced, forming SF networks as shown in Fig. 11(e). Furthermore, the mutual interaction between the SFs leads to the formation of sessile dislocations, which are generally called Lomer-Cottrell locks (L–C locks) [57] as Fig. 11(f) shows.

Fig. 12 shows the microstructures of the as-annealed alloy after tensile tests at elevated temperatures of 773 and 873 K. Generally, the density of SFs decreases while tested at 773 K. Scattered and short SFs can be observed in the CP region as Fig. 12(a) shows. The number of intersecting SFs also decreases, but they can still be observed in a few DP regions (Fig. 12(b)). As for the alloy tested at 873 K, no intersecting SFs is observed, and the density of SFs further decreases in both the CP and DP regions, as shown in Fig. 12(c, d).



### 4. Discussion

#### 4.1. The formation of the heterogeneous microstructure

As the microstructure characterization presented in Section 3.1, the as-annealed alloy exhibits a heterogeneous microstructure composed of a partially recrystallized matrix and the heterogeneous precipitated L12 phase, which can also be categorized into CP regions and DP regions. The formation mechanism of both regions during the annealing is discussed below.

The DP behavior is closely related to the migration of reaction fronts (RFs). The residual strain in the as-built alloy provides a sufficient driving force for the activation of the recrystallization [43], thus promoting the bulging and migration of grain boundaries (GBs), making them ideal RFs. Comparing Fig. 2(a, c), many newly formed fine grains are distributed around the melting track regions, indicating that recrystallization is inclined to begin around

<div style="text-align: center;">(a)</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_190_115_589_378.jpg" alt="Image" width="33%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_598_114_996_377.jpg" alt="Image" width="33%" /></div>


<div style="text-align: center;">(c)</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_190_388_589_651.jpg" alt="Image" width="33%" /></div>


<div style="text-align: center;">(d)</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_597_386_997_650.jpg" alt="Image" width="33%" /></div>


<div style="text-align: center;">Fig. 12. Typical deformation substructures in the (a) CP region and (b) DP region of the as-annealed alloy deformed at 773 K, (c) CP region, and (d) DP region of the as-annealed alloy deformed at 873 K.</div>


<div style="text-align: center;">(a)</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_287_726_593_934.jpg" alt="Image" width="25%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_601_726_907_932.jpg" alt="Image" width="25%" /></div>


<div style="text-align: center;">(c)</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_283_963_490_1137.jpg" alt="Image" width="17%" /></div>


<div style="text-align: center;">(d)</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_497_965_698_1135.jpg" alt="Image" width="16%" /></div>


<div style="text-align: center;">(e)</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_706_943_907_1142.jpg" alt="Image" width="16%" /></div>


<div style="text-align: center;">Fig. 13. (a) IPF map of the as-built alloy from the XY plane (step size = 0.05  $ \mu $m); (b) KAM map of the region corresponding to (a); (c) KAM figure from point to point corresponding to the arrow in (b); (d) cumulative KAM figure corresponding to the arrow in (b); (e) BSE observation of the as-annealed alloy from the XY plane showing the bulging of GBs.</div>


boundaries. Except for those high-angle grain boundaries (HAGBs), there are also many low-angle grain boundaries (LAGBs) and cellular boundaries in the intra-granular region. There are three general recrystallization nucleation mechanisms: strain-induced boundary migration (SIBM), sub-grain coarsening, and sub-grain coalescence [58]. The SIBM originates from HAGBs, while sub-grain coarsening and sub-grain coalescence are involved with the production of HAGBs starting from LAGBs. However, the production of HAGBs by the movement of sub-grain boundaries needs enough orientation gradient [59]. Fig. 13(a, b) shows an area from the XY plane of the as-built alloy where KAMs are distinct enough to show the contours of cellular boundaries. The point-to-point (Fig. 13(c)) and cumulative (Fig. 13(d)) changes of the orientation along the marked line in Fig. 13(b) indicate that neither the orientation gradient between cells nor the long-range orientation gradient is substantial. Therefore, it is reasonable that the recrystallization in the as-annealed alloy mostly originates from the HAGBs, which is consistent with the bulging of GBs in the as-annealed alloy (Fig. 13(e)).



During the DP process, the bulging GBs keep advancing into the original grains, and dislocations composing cellular boundaries are eliminated after GBs sweep over. The bulging GBs are also short-circuit diffusion paths for solutes and preferable nucleation.

<div style="text-align: center;"><img src="imgs/img_in_image_box_209_115_979_346.jpg" alt="Image" width="64%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_300_394_838_626.jpg" alt="Image" width="45%" /></div>


<div style="text-align: center;">Fig. 14. Schematic illustration of the microstructural evolution of the as-built alloy during the annealing: (a) The original microstructure of the as-built alloy; (b) the microstructure in the early stage of the annealing showing the bulging of the GB and the formation of the DP region; (c) the enlarged view of the CP region in the early stage of the annealing; (d) the DP region in the late stage of the annealing; (e) the enlarged view of the CP region in the late stage of the annealing.</div>


sites for the L12 phase. Once the nucleation of the L12 phase happens on the migrating grain boundaries, the precipitates will pin on the GBs. The boundary segments between the pinning precipitates keep bowing out due to the thermal activation. Meanwhile, the precipitates keep growing on the original pinning spots with the aid of rapid solute transporting from moving GBs, leading to the lamellar or short-rod morphology [60,61]. At the initial stage, the movement of bulging GBs is relatively fast, and the diffusion of solutes is limited, so the size of discontinuous precipitates in the intra-granular regions is smaller (about  $ \sim $20 nm). It should be noted that the elemental segregation along cellular boundaries is continuously promoted as the annealing process begins. The Ni, Ti, and Al segregating along the original cellular boundaries may not be completely consumed by the rapid DP. Therefore, more L12 precipitates form at the original cellular boundaries, though dislocation walls have annihilated. When the recrystallization comes to the late stage, the advance of GBs slows down, and there would be more time for the diffusion and accumulation of solutes, so precipitates near GBs exhibit larger sizes, and no cellular contour composed of precipitates can be observed (as shown in Fig. S4).

Meanwhile, without bulging GBs sweeping into the intragranular regions, the cellular structures made up of dislocations are retained, and CP dominates in the non-recrystallized grains. During the annealing process, the elemental segregation is continuously enhanced, so more L12 precipitates form along cellular boundaries, and L12 precipitates in the intra-cellular regions slowly grow up to an average size of  $ \sim $10 nm. The evolution of the microstructure during the annealing can be illustrated in the schematic drawing in Fig. 14.

### 4.2. Strengthening mechanism

In our current works, grains exhibit heterogeneous grain sizes resulting from partial recrystallization. Except for the grain sizes, the sizes of  $ L1_{2} $ precipitates and dislocation densities differ in grains in discontinuous precipitation (DP) regions and continuous precipitation (CP) regions, making the discussion about whether the as-annealed alloy is a heterostructured material necessary.



It is noteworthy that not all materials with heterogeneous microstructure can be regarded as heterostructured materials. Zhu et al. [62] indicate that heterostructured materials consist of heterogeneous zones with dramatic (> 100 %) variations in mechanical and/or physical properties and the interaction in these heterozones produces a synergistic effect where the integrated property exceeds the prediction by the rule-of-mixtures. To figure out the difference in the strength of regions in the materials, nanoindentation tests were conducted on the XY plane and XZ plane of the as-annealed alloy. 100 points were measured on each sample. The microstructure around each single nanoindentation was identified via SEM, and microstructures were classified into three categories: (1) Grains with continuous precipitates; (2) coarse recrystallized grains with discontinuous precipitates; (3) fine recrystallized grains with discontinuous precipitates, which are shown in Fig. S6. More details about the three categories of microstructure are also presented in Section 7 in Supplementary Information. The average Vicker hardness of these three kinds of microstructures on the XY plane and XZ plane is quite close, as shown in Fig. S7, indicating the as-annealed alloy in our work can be regarded as the conventional alloy.

The contribution of cellular structures is another controversial issue. The cellular structures are known to play a critical role in the optimization of mechanical properties of FCC structure alloys fabricated by selective laser melting. Earlier studies indicated that the strengthening effect of the cellular structures is Hall–Petch type [63]. However, it is found that the strength is independent of cell size, and dislocation densities of the alloy have been identified as the dominant factor in strengthening [64]. Some studies indicated that the strengthening effect of cellular structures is somehow conditional [65]. Cellular structures may be sufficiently strong against dislocation penetration and hence, behave like HAGBs, resulting in the Hall–Petch strengthening manner. Alternatively, they can be weak and only act as dislocation bundles when interacting.

with moving dislocations, resulting in a dislocation-like strengthening manner. As Fig. 10(b) shows, the cellular boundaries composed of tangled dislocations may decompose at high strain, indicating the cellular boundaries in the as-built alloy are not as strong as grain boundaries. The KAM map of the as-built alloy shown in Fig. 13(b) suggests that the cellular boundaries here can only cause limited local misorientations, which cannot be even regarded as LAGBs. Therefore, the contribution of cellular boundaries here is attributed to the dislocation hardening.

Based on the microstructural characterization, the increase in the yield strength of the as-annealed alloy can be ascribed to the contribution of solid solution hardening ( $ \Delta\sigma_{ss} $), grain boundary hardening ( $ \Delta\sigma_{gb} $), dislocation hardening ( $ \Delta\sigma_{dis} $), and precipitation hardening ( $ \Delta\sigma_{ppt} $), in addition to the matrix friction stress ( $ \sigma_{fr} $). Therefore, the yield strength of the as-built alloy and the as-annealed alloy at 298 K can be demonstrated by the following equation:

 $$ \sigma_{\mathrm{y-as~built}}=\sigma_{\mathrm{fr}}+\Delta\sigma_{\mathrm{ss}}+\Delta\sigma_{\mathrm{gb}}+\Delta\sigma_{\mathrm{dis}}, $$ 

 $$ \sigma_{\mathrm{y-as annealed}}=\sigma_{\mathrm{fr-matrix}}+\Delta\sigma_{\mathrm{ss}}+\Delta\sigma_{\mathrm{gb}}+\Delta\sigma_{\mathrm{dis}}+\Delta\sigma_{\mathrm{ppt}}, $$ 

For the as-built alloy, the friction stress ( $ \sigma_{fr} $) is determined as 218 MPa by using the friction stress of the equiatomic CoCrNi alloy [66]. For the as-annealed alloy,  $ \sigma_{fr-matrix} $ should multiply the volume fraction of the FCC matrix phase ( $ f_{matrix} $).

 $$ \sigma_{\mathrm{f r-m a t r i x}}=\sigma_{\mathrm{f r}}\cdot f_{\mathrm{m a t r i x}}, $$ 

 $$ f_{matrix}=1-f_{ppt}, $$ 

 $$ f_{\mathrm{p p t}}=P_{\mathrm{D P}}\cdot f_{\mathrm{d p}}+P_{\mathrm{C P}}\cdot f_{\mathrm{c p}}. $$ 

where  $ f_{ppt} $ is the volume fraction of precipitates.  $ P_{DP} $ is the volume fraction of the discontinuous precipitation region to the whole matrix, and  $ P_{CP} $ is the volume fraction of the continuous precipitation region to the matrix.  $ f_{dp} $ is the volume fraction of discontinuous precipitates in the discontinuous precipitation region,  $ f_{cp} $ is the volume fraction of continuous precipitates in the continuous precipitation region.

$P_{\mathrm{DP}}$ and $P_{\mathrm{CP}}$ are estimated to be 77.6 % and 22.4 % via SEM figures, respectively. $f_{\mathrm{dp}}$ is calculated to be 28.3 % by using the lever rule. However, continuous precipitates are too small to attain reliable chemical composition via TEM. The previous study indicates that the difference in volume fractions of $L1_2$ precipitates in different regions of the heterogeneous matrix is less than 2 % [6]. Hence, the $f_{\mathrm{cp}}$ is regarded to be equal to 28.3 %. It follows that $f_{\mathrm{ppt}}$ and $f_{\mathrm{matrix}}$ are 28.3% and 71.7 %, respectively, thus $\sigma_{\mathrm{fr-matrix}} = 218 \times 71.7\% = 156.3$ MPa.

The strengthening effect from solid-solution ( $ \Delta\sigma_{ss} $) can be calculated by the standard model based on the interactions between dislocations and the substitutional solute atoms [3]:

 $$ \Delta\sigma_{ss}=M\frac{G\cdot\varepsilon_{s}^{3/2}\cdot c^{1/2}}{700}, $$ 

 $$ \varepsilon_{s}=\left|\frac{\varepsilon_{G}}{1+0.5\varepsilon_{G}}-3\cdot\varepsilon_{a}\right|, $$ 

 $$ \varepsilon_{\mathrm{a}}=\frac{1}{a_{\mathrm{m}}}\frac{\partial a}{\partial c}. $$ 

where M is the Taylor factor, here M = 3.06 for FCC metals [3]; G is the shear modulus, here G = 88.7 GPa (borrowed from the equiatomic CoCrNi MEA [67]);  $ a_{m} $ is the lattice constant of the matrix, here  $ a_{m} = 0.357 $ nm (borrowed from the equiatomic CoCrNi MEA [67]); c is the molar ratio of the solute atoms, here c should be the total molar ratio of Ti and Al. Based on the STEM-EDS measurement, on the as-built and as-annealed alloys, values of c are 7.49 % and 2.07 %, respectively.  $ \varepsilon_{s} $ is the interaction factor.  $ \varepsilon_{G} $ and  $ \varepsilon_{a} $ are interaction parameters that are related to elastic size mismatch and atomic mismatch, respectively. Compared with  $ \varepsilon_{a} $, the effect of  $ \varepsilon_{G} $ is negligible, so the  $ \varepsilon_{s} $ can be generally treated as  $ 3\varepsilon_{a} $,  $ \Delta\sigma_{ss} $ can be approximately regarded to be proportional to  $ c^{1/2} $. The  $ \Delta\sigma_{ss} $ of the solid-solution-state (CoCrNi) $ _{94} $Al $ _{3} $Ti $ _{3} $ alloy was estimated to be  $ \sim49 $ MPa [54]. Hence, the strengthening effect of solid-solution ( $ \Delta\sigma_{ss} $) for as-built and as-annealed alloys is calculated to be 61.2 and 16.9 MPa, respectively, indicating the solid-solution hardening contribution is quite limited.



The strengthening contribution from grain boundaries ( $ \Delta\sigma_{gb} $) can be calculated by using the classical Hall–Petch formula:

 $$ \Delta\sigma_{\mathrm{g b}}=k_{\mathrm{g b}}\cdot d^{-1/2} $$ 

where  $ k_{gb} $ is the strengthening coefficient, and d is the average grain size.  $ k_{gb} = 568 $ MPa  $ \mu $m $ ^{-1/2} $ [54], and the average grain size for the as-built and as-annealed alloy is 11.9 and 3.5  $ \mu $m, respectively. Thus,  $ \Delta\sigma_{gb} $ for the as-built and as-annealed alloys are calculated to be 164.3 and 303.6 MPa, respectively.

The  $ \Delta\sigma_{dis} $ can be estimated by the following equation [68]:

 $$ \Delta\sigma_{\mathrm{d i s}}=M\alpha G b\rho^{1/2}, $$ 

 $$ \rho_{\mathrm{GND}}=\frac{2\theta}{u b}. $$ 

where  $ \alpha = 0.2 $ for FCC metals [69]; b is the Burgers vector ( $ b = 0.2532 \times 10^{-9} $ m for the as-built alloy, and  $ b = 0.2527 \times 10^{-9} $ m for the as-annealed alloy, which are calculated from the XRD pattern).  $ \rho $ represents the density of GNDs.  $ \theta $ is the KAM value obtained from the KAM maps, here we use the average of KAM values acquired from the XY plane and the XZ plane of the as-built alloy and the as-annealed alloy (Fig. S3).  $ \theta_{as-built} = 0.45^\circ $,  $ \theta_{as-annealed} = 0.395^\circ $.  $ \mu $ is the unit length for EBSD characterization, here  $ \mu = 0.2 $  $ \mu $m. Based on KAMs, the dislocation density is calculated:  $ \rho_{as-built} = 3.10 \times 10^{14} $ m $ ^{-2} $, and  $ \rho_{as-annealed} = 2.73 \times 10^{14} $ m $ ^{-2} $. Hence,  $ \Delta \sigma_{dis} $ for the as-built and as-annealed alloys are calculated to be 242.0 and 225.4 MPa, respectively.

The  $ \Delta\sigma_{ppt} $ is given by the ordering strengthening [70]:

 $$ \Delta\sigma_{\mathrm{p p t}}=0.81M\frac{\gamma_{\mathrm{A P B}}}{2b}\left(\frac{3\pi f}{8}\right)^{1/2} $$ 

where $f$ is the volume fraction of precipitates, $f = 28.3\%$; $\gamma_{\mathrm{APB}}$ is the antiphase boundary energy, here $\gamma_{\mathrm{APB}} = 143\,\mathrm{mJ}\,\mathrm{m}^{-2}$ [6]. Therefore, the $\Delta\sigma_{\mathrm{ppt}}$ at 298 K is calculated to be 404.8 MPa.

According to the investigation on the yield strength at different temperatures, the friction stress of the matrix versus temperature can be expressed as [2]:

 $$ \sigma_{\mathrm{f}}(T)=\frac{2G}{1-\nu}\exp\left(\frac{-2\pi\omega_{0}}{b}\right)\cdot\exp\left(\frac{-2\pi\omega_{0}}{bT_{\mathrm{m}}}T\right) $$ 

where  $ \nu $ is the Poisson's ratio,  $ \omega_0 $ is the dislocation width at 0 K, b is the Burgers vector, T is the testing temperature, and  $ T_m $ is the melting temperature. Note that b is regarded as the temperature-independent term since the change of b with temperature is very small. However,  $ G_{\text{FCC}} $ and  $ \nu $ are temperature-dependent terms. By using  $ \sigma_{\text{fr}} $ (298 K) = 218 MPa,  $ G_{\text{FCC}}(298 \text{ K}) = 88.7 \text{ GPa} $,  $ \nu $ (298 K) = 0.314 [71],  $ T_m = 1664 \text{ K} $ [6], the  $ \omega_0 $ is calculated to be 0.958b. At 77 K,  $ G_{\text{FCC}}(77 \text{ K}) = 93.5 \text{ GPa} $ [67],  $ \nu(77 \text{ K}) = 0.308 $ [71], thus the  $ \sigma_{\text{fr}} $ values for the as-built and as-annealed alloy are calculated to be 498.9 and 357.7 MPa, respectively.

 $ \Delta\sigma_{gb} $ and  $ \Delta\sigma_{ppt} $ are considered to be temperature-independent for the as-built or the annealed specimens when tested at 298 or 77 K, since the grain size and precipitate volume fraction are postulated to be fixed at these two test temperatures. For  $ \Delta\sigma_{ss} $, if the change of  $ \varepsilon_s $ with temperature is ignored, the

<div style="text-align: center;"><img src="imgs/img_in_chart_box_234_112_956_613.jpg" alt="Image" width="60%" /></div>


<div style="text-align: center;">Fig. 15. The contributions of different strengthening mechanisms to YS of the as-built alloy and the as-annealed alloy, and the comparison between calculated values and experimental values.</div>


 $ \Delta\sigma_{ss} $ for as-built and as-annealed alloys are calculated to be 64.5 and 17.8 MPa, respectively.  $ \Delta\sigma_{dis} $ would also change with the temperature due to the change of G. With the changed G,  $ \Delta\sigma_{dis} $ at 77 K for the as-built and as-annealed alloy are calculated to be 255.1 and 237.6 MPa, respectively.

The contribution from all the strengthening effects mentioned above is displayed in Fig. 15. The calculation results are well agreed with the experimental results. Precipitation hardening makes the most contribution for the as-annealed alloy at 298 and 77 K, and grain boundary strengthening and dislocation strengthening resulting from additive manufacturing takes the second place, exhibiting the excellent combination of precipitation hardening and the advantage of additive manufacturing.

### 4.3. Temperature-dependent strain-hardening rate

The strain-hardening rate of the as-built and the as-annealed alloy show evident temperature dependence, as presented in Fig. 9(b). For the as-built alloy, the planar dislocation glide is the dominant deformation mode at 298 K. While at 77 K, a large number of SFs are generated via dislocation dissociation, and DTs are also activated. SFs and DTs provide more resistance to the dislocation slip by decreasing the mean free path of dislocations, which is called the dynamic Hall-Petch effect [72–74] so that the as-built alloy shows higher strain-hardening rate, strength, and ductility at 77 K.

For the as-annealed alloy, the planar dislocation glide acts as the main deformation mechanism from 77 to 873 K, and no DT is observed. The fully coherent interface between the high density of  $ L_{12} $ precipitates and the FCC matrix can relieve stress concentration [10], providing a higher strain-hardening rate and maintaining a respectable uniform plastic deformation at the same time. The increase in the number of SFs at 77 K leads to a decreasing SF spacing size and more SF networks, which are confirmed to be significantly effective in impeding the movement of dislocations and retaining strain-hardening [74,75]. On the other hand, the L-C lock generated by the interactions between SFs can further hinder the moving dislocations and provide more dislocations to accommodate plastic deformation by serving as Frank-Read dislocation sources [57]. Furthermore, the APBs formed by the interaction between SFs and  $ L_{12} $ precipitates can act as barriers against dislocation mobility, which can further increase the strain-hardening rate [76]. Hence, the as-annealed alloy shows the best synergy of strength and ductility at 77 K, and a much higher strain-hardening rate is obtained at 77 K in comparison with that at 298 K. When the test temperature increases to 773 and 873 K, the strength of the as-annealed alloy decreases together with the density of SFs.



Accordingly, the strain hardening rate of the as-annealed alloy is SFs-mediated, which is closely associated with the SFE as the following equation describes [77]:

 $$ \tau_{SF}=\frac{2\gamma_{SF}}{b_{p}} $$ 

where  $ \gamma_{SF} $ is the SFE,  $ \tau_{SF} $ is the critical resolved shear stress required for spontaneous partial dislocation separation and associated extended SF formation, and  $ b_{p} $ is the Burgers vector of a Shockley partial dislocation. The stacking fault energy ( $ \gamma_{SF} $) of the FCC matrix at 298 K can be estimated using the following equation [78]:

 $$ \gamma_{\mathrm{S F}}=n\rho_{\mathrm{A}}\varDelta G^{\mathrm{F C C\rightarrow H C P}}+2\sigma^{\mathrm{F C C/H C P}} $$ 

where $n$ is the number of fault layers, i.e., $n = 2$ for an intrinsic stacking fault, $\rho_A$ is the molar surface density, $\Delta G^{FCC \rightarrow HCP}$ is the difference in Gibbs free energy of FCC and HCP phases, and $\sigma^{FCC/HCP}$ is the interfacial energy between FCC and HCP phases, which is assumably $10 \pm 5$ mJ m$^{-2}$ for transition metals [79]. For {111}, $\rho_A$ is defined as:

 $$ \rho_{\mathrm{A}}=\frac{4}{\sqrt{3}a_{\mathrm{FCC}}^{2}}\frac{1}{N_{\mathrm{A}}} $$ 

where  $ a_{FCC} $ is the lattice constant of the FCC phase, which is 0.3571 nm according to the deconvolution of the (311) XRD peak, as shown in Fig. S8, and  $ N_{A} $ is the Avogadro constant. Therefore,  $ \rho_{A} $ is calculated to be  $ 3 \times 10^{-5} $ mol m $ ^{-2} $. By performing chemical composition-based thermodynamic calculation using ThermoCalc (TCHEA5 database), the left unknown parameter in Eq. (15),

<div style="text-align: center;">Table 2 The chemical compositions acquired via TEM-EDS and lattice constants acquired from XRD of FCC and L12 phases.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td rowspan="2">Phase</td><td colspan="5">Composition (at.%)</td><td rowspan="2">Lattice constant (nm)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Co</td><td style='text-align: center; word-wrap: break-word;'>Cr</td><td style='text-align: center; word-wrap: break-word;'>Ni</td><td style='text-align: center; word-wrap: break-word;'>Al</td><td style='text-align: center; word-wrap: break-word;'>Ti</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>FCC</td><td style='text-align: center; word-wrap: break-word;'>50.84</td><td style='text-align: center; word-wrap: break-word;'>25.55</td><td style='text-align: center; word-wrap: break-word;'>21.54</td><td style='text-align: center; word-wrap: break-word;'>1.00</td><td style='text-align: center; word-wrap: break-word;'>1.07</td><td style='text-align: center; word-wrap: break-word;'>0.3571</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ L1_{2} $</td><td style='text-align: center; word-wrap: break-word;'>16.01</td><td style='text-align: center; word-wrap: break-word;'>4.38</td><td style='text-align: center; word-wrap: break-word;'>59.12</td><td style='text-align: center; word-wrap: break-word;'>9.77</td><td style='text-align: center; word-wrap: break-word;'>10.71</td><td style='text-align: center; word-wrap: break-word;'>0.3595</td></tr></table>

 $ \Delta G^{\text{FCC} \rightarrow \text{HCP}} $ can be determined as follows:

 $$ \begin{aligned}\Delta G^{\mathrm{FCC\rightarrow HCP}}&=G^{\mathrm{HCP}}-G^{\mathrm{FCC}}=-755.808-(-834.538)\\&=78.73\mathrm{J}\ \mathrm{mol}^{-1}\end{aligned} $$ 

where  $ G^{FCC} $ and  $ G^{HCP} $ are the total energies of FCC and HCP structures based on the composition of the FCC phase in the current alloy, as listed in Table 2. By substituting Eqs. (16) and (17) as well as other derived parameters into Eq. (15),  $ \gamma_{SF} $ is estimated as  $ 25 \pm 10 $ mJ m $ ^{-2} $. At room temperature, this value may be too high to activate twinning, but reasonably low enough to introduce pronounced slip planarities such as SF networks and L-C locks in the FCC phase [80], which can be further confirmed by calculating the critically resolved shear stress ( $ \tau_{SF} $) to initiate SFs in the matrix of the present alloy by Eq. (14). Here  $ b_{p} $ is the Burgers vector of 1/6<112> partial dislocations (0.1458 nm). Thus,  $ \tau_{SF} $ is computed to be 343 MPa, and the critical stress ( $ \sigma_{SF} $) is estimated to be 1043 MPa by multiplication of Taylor factor (M = 3.06 [3]), i.e.,  $ \sigma_{SF} = M\tau_{SF} $, which is well below the YS and flow stress of as-annealed alloy (1180 MPa), resulting in observed SFs at room temperature.

Additionally, the possibility of SFs penetrating through L1₂ precipitates in the as-annealed alloy at 298 K is theoretically evaluated as follows. Consider that L1₂ can be shorn by dislocations, i.e., the flow stress is larger than the precipitate shearing stress ( $ \Delta\sigma_{ppt} = 405 $ MPa, which is calculated via Eq. (12)), which is also evidenced by TEM observation (Fig. S9), for most Ni-based and NiCo-based superalloys, a superlattice intrinsic stacking fault (SISF) may form when the L1₂ precipitate interacts with two 1/2<110> dislocations in the matrix according to the following equation [81]:

 $$ \frac{1}{2}[0\bar{1}1]+\frac{1}{2}[1\bar{1}0]\rightarrow\frac{1}{3}[1\bar{2}1]+S I S F+\frac{1}{6}[1\bar{2}1] $$ 

where the leading 1/3<112> dislocation enters the precipitate, while a 1/6<112> is left at the interface. The corresponding resolved shear stress ( $ \tau_{SISF} $) can be expressed by the following equation [82]

 $$ \tau_{SISF}=\frac{\gamma_{SISF}}{b_{1}}-\frac{G_{S}a_{S}^{2}}{6\pi b_{1}r(1-\nu_{S})} $$ 

where  $ \gamma_{SISF} $ is the SISF energy,  $ b_l $ is the Burgers vector of the leading  $ 1/3 < 112 > $ dislocation (0.2935 nm here),  $ r $ is the dislocation separation distance,  $ G_s $,  $ a_s $, and  $ v_s $ are shear modulus (89.2 GPa [83]), lattice constant (0.3595 nm here), and Poison's ratio ( $ \sim 0.2 $ [84]) of the L12 phase, respectively. By taking the range of  $ \gamma_{SISF} $ (from  $ \sim 50 $ mJ m $ ^{-2} $ for Ni-based to  $ \sim 100–150 $ mJ m $ ^{-2} $ for Co-based superalloys [85]) into account, the applied flow stress against  $ r $ can be plotted using  $ \sigma_{SISF} = M\tau_{SISF} $, as shown in Fig. 16, which indicates that the SFs can be activated in L12 precipitates at room temperature.

It has been reported that the SFEs of FCC alloys and MPEAs increase with increasing temperature. At 77 K, the SFE is lower than that at room temperature. The lower the SFE, the lower the  $ \sigma_{SF} $, so that more SFs are activated, forming SF networks and L-C locks and leading to the ultra-high strain hardening rate. As temperature increases to 773 and 873 K, the SFE is higher than that at

<div style="text-align: center;"><img src="imgs/img_in_chart_box_669_111_1056_410.jpg" alt="Image" width="32%" /></div>


<div style="text-align: center;">Fig. 16. The estimated critical flow stress  $ \sigma_{SISF} $ for the onset of SFs in the L12 phases with different  $ \gamma_{SISF} $ vs. the dislocation separation distance (r).</div>


room temperature, thus the  $ \sigma_{SF} $ also increases, leading to the decreasing numbers of SFs and strain-hardening rate. Therefore, the as-annealed alloy exhibits a temperature-dependent strain hardening rate, which stems from the variation of SFE with temperature [86,87].

However, it should be pointed out that the variation of SFE with temperature is not the only influence that decides the temperature-dependent strain-hardening behavior of alloys. Pierce et al. [88] reported that the increase in the SFE with the increasing temperature (from RT to 400 °C) of the Fe-22/25/28Mn-3Al-3Si (wt%) alloys causes the transition from planar to wavy dislocation glide and the decrease in the work hardening rate from 0 to 0.1 true strain when the twinning has not been activated, which is consistent with the as-annealed alloy here. However, for the mechanical twinning, although the critical resolved shear stress (CRSS) for mechanical twinning estimated from microstructure and strain hardening behavior show substantial temperature dependence, the increase in SFE with temperature had a rather minor influence on the CRSS for twinning. The decrease in friction stress of alloys with the elevated temperature is considered one of the reasons for the late activation of twinning at elevated temperatures. The reducing friction stress is revealed to facilitate the cross slip [89], which in turn reduces the local stress concentrations and delays the initiation of mechanical twinning to higher normal stress levels.

It is worth mentioning that mechanical properties at elevated temperatures may also be affected by dynamic recovery (DRV) and dynamic recrystallization (DRX). Fig. 17 shows the deformed microstructure from the XZ plane of the as-annealed alloy tested at 773 K (Fig. 17(a, b)) and 873 K (Fig. 17(c, d)). The alloy tested at 773 K exhibits a higher density of GNDs, which is consistent with its better ductility. Compared with the microstructure before deformation, the average grain sizes show little change, and the GNDs densities increase. The grain size distribution map and KAM distribution maps are shown in Fig. S10. Moreover, both of the tensile curves tested at 773 and 873 K in Fig. 9 did not exhibit softening before the fracture, indicating no evident DRX happens till the fracture. Although DRX contributes little to the decrease of the strength, the climbing of dislocations would be enhanced at elevated temperatures due to thermal activation, thus deteriorating the effect of dislocation strengthening and leading to the decreasing strength of the as-annealed alloy [23,59].

The fracture surface of the tensile alloys tested at 773 and 873 K exhibit mixed fracture mode (Fig. 18(a, e)). Dimples prevail in a large area as Fig. 18(b, c, f, g) shows, which is consistent with the decent ductility. However, there are also typical cleavage facets with intergranular cracks around (Fig. 18(d, h)), indicating

<div style="text-align: center;"><img src="imgs/img_in_image_box_190_116_997_384.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Fig. 17. EBSD results of the deformed microstructures for the as-annealed alloys tested at 773 and 873 K (step size = 0.2  $ \mu $m). The IPF map from the XZ plane of the as-annealed alloy tested at (a) 773 K and (c) 873 K; The KAM map from the XZ plane of the as-annealed alloy tested at (b) 773 K and (d) 873 K.</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_215_466_976_845.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Fig. 18. SEM fractography of the as-annealed alloy tested at 773 K in (a), with the enlarged views shown in (b–d); at 873 K in (e), with the enlarged views shown in (f–h).</div>


that the coarse discontinuous precipitates along grain boundaries are responsible for the decrease of elongation at elevated temperatures [36,90]. It is noteworthy that the considerable decrease of elongation at intermediate temperatures commonly exists in polycrystalline alloys, such as Ni-based superalloys, which are referred to as intermediate-temperature embrittlement [91]. Intergranular precipitates, grain boundary shearing or sliding, gas phase embrittlement, decohesion of glide plane, dynamic strain aging, and grain boundary segregation of impurities are the main existing interpretations for the intermediate-temperature embrittlement. The coarse discontinuous precipitates along grain boundaries should not be the only reason for the intermediate-temperature embrittlement of the as-annealed alloy, and the clarification of other mechanisms needs further studies in the future.

No DT has been found in the  $ Co_{42}Cr_{20}Ni_{30}Ti_{4}Al_{4} $ MEAs after deformation, except for the as-built alloy deformed at 77 K, which is different from some CoCrNi MEAs and CoCrNiTiAl MEAs that are dominated by DT at room temperature [30,54–56]. The activation of twinning is often thought to be relevant to the low SFE [55,92]. It has been revealed that the addition of Ti and Al can increase the SFE of the alloy [93,94], making it more difficult to activate DTs at room temperature for the as-built alloy which is in the solid solution state. However, when it turns to the cryogenic temperature, the SFE would decrease with the lower temperature as indicated by previous studies [87,95], and more SFs contribute to higher flow stress, making the activation of DT possible and finally leading to significantly improved ductility.

Meanwhile, it has been reported that the twin initiation stress can also be affected by the grain size [96]. The relationship can be described by the following equation [97]:



 $$ \sigma_{\mathrm{T}}=M\frac{\gamma}{b_{\mathrm{p}}}+\frac{k_{\mathrm{T}}}{\sqrt{d}} $$ 

where  $ \sigma_T $ is the critical twinning stress,  $ M $ is the Taylor factor,  $ \gamma $ is the SFE,  $ b_p $ is the Burgers vector of a partial dislocation,  $ k_T $ is the Hall-Petch constant for twinning, and  $ d $ is the grain size. After the annealing, the average grain size decreases from 9.6 to 3.5  $ \mu $m due to the recrystallization as shown in Fig. 2, thus the inhibition of DTs is enhanced due to the increased critical shear stress. Furthermore, the drastically reduced channel width of the FCC matrix due to the high density of  $ L_1_2 $ precipitates makes it even harder to activate DTs for the as-annealed alloy even at cryogenic temperature, which is supported by other reported  $ L_1_2 $ precipitation-strengthened CoCrNi-based MEAs whose deformation are mainly SFs mediated [30,54,74,98]. Moreover, the  $ L_1_2 $-type precipitates possess much higher SFE compared to the FCC matrix, so that the incorporation of  $ L_1_2 $ precipitates would substantially increase the global SFE of the alloy, and subsequently increase the critical stress for twinning nucleation, leading to the suppression of the DT initiation [74,99].

### 5. Conclusions

In the present work, we successfully developed a precipitation hardening  $ Co_{42}Cr_{20}Ni_{30}Ti_{4}Al_{4} $ MEA via SLM and the post-

heat treatment, exhibiting an excellent strength-ductility combination from 77 to 873 K. The strengthening mechanisms and the temperature-dependent strain-hardening rate were explored and discussed. The following conclusions can be drawn:

(1) The microstructures are composed of the partially recrystallized matrix and heterogeneous precipitation of the  $ L1_{2} $ phase, stemming from the concurrence of recrystallization and precipitation during the post-heat treatment. Discontinuous precipitation of the  $ L1_{2} $ phase takes place where recrystallization occurs, and continuous precipitation takes place at nonrecrystallized regions. Cellular boundaries composed of dislocations are preferable nucleation sites for the  $ L1_{2} $ phase but do not act as nucleation sites for the recrystallization as high-angle grain boundaries due to the limited misorientations.

(2) The as-annealed MEA exhibits a superiority of mechanical properties over a wide temperature ranging from 77 to 873 K among the reported additively manufactured alloys, especially with an excellent YS of 1180 MPa, UTS of 1586 MPa with total elongation of 22.7 % at 298 K, as well as an ultra-high YS of 1341 MPa, UTS of 1944 MPa with total elongation of 22.6 % at 77 K. The synergy of precipitation hardening, grain boundaries hardening, and dislocation hardening contributes to the high yield strength, showing a successful combination of precipitation hardening and additive manufacturing technology.

(3) Planar dislocation slip is the main deformation mechanism of the as-annealed MEA from 77 to 873 K. The decrease of SFs with increasing temperature could be ascribed to the SFE increasing with increasing temperature so that the strain-hardening rate exhibits temperature dependency. The high strain-hardening rate at 77 K results from the nano-spaced SFs networks, Lomer-Cottrell locks, and APBs, which are brought by the high density of SFs.

(4) No substantial softening and DRX have occurred in the as-annealed alloy at elevated temperatures over 773 to 873 K. The coarse discontinuous L1₂ precipitates along grain boundaries would induce the intergranular fracture, leading to premature tensile failure at 773 and 873 K.

(5) Compared to the as-built alloy at the state of solid solution, no DT is found in the as-annealed alloy. It may be ascribed to the increasing critical twinning stress derived from the fine channel width, small grain size, and the high SFE of the L12 phase.