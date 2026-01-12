#
# MANIPURAKA RAPE REPAIR: A simple Python
#
#
#

from __future__ import annotations

import re
from typing import Final, Pattern
import argparse


# Pre-compile once (module-level) for performance.
# NOTE:
# - We avoid \b because it behaves poorly for Devanagari/Urdu boundaries.
# - We instead use a "safe boundary" on both sides:
#   (^|[^\w\u0900-\u097F\u0600-\u06FF]) ... (?=$|[^\w\u0900-\u097F\u0600-\u06FF])
MANIPURAKA_RAPE_PATTERN: Final[Pattern[str]] = re.compile(
    r"(?is)"
    r"(^|[^\w\u0900-\u097F\u0600-\u06FF])"
    r"("
    # =========================
    # ENGLISH CORE + EXPANSIONS
    # =========================
    r"r(?:a|@|4)\s*[_\-\.\s]*p\s*[_\-\.\s]*e(?:d|s|r|rs|ing)?"
    r"|rapist(?:s)?"
    r"|sexual\s*assault|sexually\s*assault(?:ed)?"
    r"|sexual\s*abuse|sexually\s*abus(?:e|ed)"
    r"|mol(?:e|3|0)\s*[_\-\.\s]*s\s*[_\-\.\s]*t(?:ed|ation|ing)?"
    r"|molestation"
    r"|grop(?:e|ed|ing)"
    r"|fondl(?:e|ed|ing)"
    r"|non[-\s]*consensual|without\s*consent"
    r"|coerc(?:e|ed|ion|ing)"
    r"|forced\s*sex|force(?:d|fully)\s*(?:sex)?"
    r"|statutory\s*rape"
    r"|incest(?:uous)?"
    r"|child\s*(?:sexual\s*)?abuse"
    r"|c\s*[\.\-_ ]?\s*s\s*[\.\-_ ]?\s*a"
    r"|minor\s*(?:sexual\s*)?abuse"
    r"|sex\s*traffick(?:ing|ed)?|traffick(?:ing|ed)\s*(?:sex)?"
    # ==================================
    # HINDI (DEVANAGARI) + COMMON FORMS
    # ==================================
    r"|बलात्कार"
    r"|दुष्कर्म"
    r"|यौन\s*शोषण"
    r"|यौन\s*(?:उत्पीड़न|उत्पीडन)"
    r"|छेड़छाड़|छेडछाड"
    r"|जबरन\s*संभोग"
    r"|अश्लील\s*हरकत"
    r"|बाल\s*यौन\s*शोषण"
    r"|नाबालिग\s*(?:यौन\s*)?शोषण"
    r"|पोक्सो|pocso"
    # ===========================================
    # HINGLISH / ROMANIZED HINDI (ONLINE COMMON)
    # ===========================================
    r"|bala?tkar(?:i)?"
    r"|dushkarm"
    r"|yaun\s*(?:shoshan|utpeedan|utpidan)"
    r"|chhe?d\s*chha?d|chedchad|chhedchhad"
    r"|jabran\s*sambhog"
    r"|zabardasti\s*(?:sex|sexx|s3x)?"
    r"|sex\s*ke\s*liye\s*majboor|majboori\s*se\s*sex"
    # =====================
    # URDU (ARABIC SCRIPT)
    # =====================
    r"|زیادتی"
    r"|جنسی\s*زیادتی"
    r"|جنسی\s*تشدد"
    r"|بچوں\s*کا\s*جنسی\s*استحصال"
    r"|زبردستی\s*ہمبستری"
    r")"
    r"(?=$|[^\w\u0900-\u097F\u0600-\u06FF])"
)

RAPE_DICTIONARY = [
    "1nc357",
    "1nc357_357upr0",
    "357upr0",
    "4bu5 53xu3l",
    "4bu5 53xu3l_4bu50 53xu4l",
    "4bu50 53xu4l",
    "4gr35510n 53xu3ll3",
    "4gr35510n 53xu3ll3_53x 7r4ff1ck1ng",
    "53x 7r4ff1ck1ng",
    "53xu3ll3r m155br4uch",
    "53xu3ll3r m155br4uch_53xu4l 4554ul7",
    "53xu4l 4554ul7",
    "53xu4l 4bu53",
    "53xu4l 4bu53_5747u70ry r4p3",
    "5747u70ry r4p3",
    "57upr0",
    "57upr0_a b u s o s e x u a l",
    "a b u s o s e x u a l",
    "a b u s s e x u e l",
    "a b u s s e x u e l_a g r e s s i o n s e x u e l l e",
    "a g r e s s i o n s e x u e l l e",
    "a-b-u-s-o-s-e-x-u-a-l",
    "a-b-u-s-o-s-e-x-u-a-l_a-b-u-s-s-e-x-u-e-l",
    "a-b-u-s-s-e-x-u-e-l",
    "a-g-r-e-s-s-i-o-n-s-e-x-u-e-l-l-e",
    "a-g-r-e-s-s-i-o-n-s-e-x-u-e-l-l-e_a.b.u.s.o.s.e.x.u.a.l",
    "a.b.u.s.o.s.e.x.u.a.l",
    "a.b.u.s.s.e.x.u.e.l",
    "a.b.u.s.s.e.x.u.e.l_a.g.r.e.s.s.i.o.n.s.e.x.u.e.l.l.e",
    "a.g.r.e.s.s.i.o.n.s.e.x.u.e.l.l.e",
    "a_b_u_s_o_s_e_x_u_a_l",
    "a_b_u_s_o_s_e_x_u_a_l_a_b_u_s_s_e_x_u_e_l",
    "a_b_u_s_s_e_x_u_e_l",
    "a_g_r_e_s_s_i_o_n_s_e_x_u_e_l_l_e",
    "a_g_r_e_s_s_i_o_n_s_e_x_u_e_l_l_e_abus sexuel",
    "abus sexuel",
    "abuso sexual",
    "abuso sexual_abusosexual",
    "abusosexual",
    "abussexuel",
    "abussexuel_agresión sexual",
    "agresión sexual",
    "agression sexuelle",
    "agression sexuelle_agressionsexuelle",
    "agressionsexuelle",
    "agressão sexual",
    "agressão sexual_b a l a t k a r",
    "b a l a t k a r",
    "b-a-l-a-t-k-a-r",
    "b-a-l-a-t-k-a-r_b.a.l.a.t.k.a.r",
    "b.a.l.a.t.k.a.r",
    "b4l47k4r",
    "b4l47k4r_b_a_l_a_t_k_a_r",
    "b_a_l_a_t_k_a_r",
    "balatkar",
    "balatkar_c h h e d c h h a d",
    "c h h e d c h h a d",
    "c h i l d s e x u a l a b u s e",
    "c h i l d s e x u a l a b u s e_c o e r c i o n",
    "c o e r c i o n",
    "c s a",
    "c s a_c-h-h-e-d-c-h-h-a-d",
    "c-h-h-e-d-c-h-h-a-d",
    "c-h-i-l-d-s-e-x-u-a-l-a-b-u-s-e",
    "c-h-i-l-d-s-e-x-u-a-l-a-b-u-s-e_c-o-e-r-c-i-o-n",
    "c-o-e-r-c-i-o-n",
    "c-s-a",
    "c-s-a_c.h.h.e.d.c.h.h.a.d",
    "c.h.h.e.d.c.h.h.a.d",
    "c.h.i.l.d.s.e.x.u.a.l.a.b.u.s.e",
    "c.h.i.l.d.s.e.x.u.a.l.a.b.u.s.e_c.o.e.r.c.i.o.n",
    "c.o.e.r.c.i.o.n",
    "c.s.a",
    "c.s.a_c03rc10n",
    "c03rc10n",
    "c54",
    "c54_c_h_h_e_d_c_h_h_a_d",
    "c_h_h_e_d_c_h_h_a_d",
    "c_h_i_l_d_s_e_x_u_a_l_a_b_u_s_e",
    "c_h_i_l_d_s_e_x_u_a_l_a_b_u_s_e_c_o_e_r_c_i_o_n",
    "c_o_e_r_c_i_o_n",
    "c_s_a",
    "c_s_a_ch1ld 53xu4l 4bu53",
    "ch1ld 53xu4l 4bu53",
    "chh3dchh4d",
    "chh3dchh4d_chhedchhad",
    "chhedchhad",
    "child sexual abuse",
    "child sexual abuse_childsexualabuse",
    "childsexualabuse",
    "cinsel saldırı",
    "cinsel saldırı_coercion",
    "coercion",
    "csa",
    "csa_d u s h k a r m",
    "d u s h k a r m",
    "d-u-s-h-k-a-r-m",
    "d-u-s-h-k-a-r-m_d.u.s.h.k.a.r.m",
    "d.u.s.h.k.a.r.m",
    "d_u_s_h_k_a_r_m",
    "d_u_s_h_k_a_r_m_du5hk4rm",
    "du5hk4rm",
    "dushkarm",
    "dushkarm_e s t u p r o",
    "e s t u p r o",
    "e-s-t-u-p-r-o",
    "e-s-t-u-p-r-o_e.s.t.u.p.r.o",
    "e.s.t.u.p.r.o",
    "e_s_t_u_p_r_o",
    "e_s_t_u_p_r_o_estupro",
    "estupro",
    "f o r c e d s e x",
    "f o r c e d s e x_f-o-r-c-e-d-s-e-x",
    "f-o-r-c-e-d-s-e-x",
    "f.o.r.c.e.d.s.e.x",
    "f.o.r.c.e.d.s.e.x_f0rc3d 53x",
    "f0rc3d 53x",
    "f_o_r_c_e_d_s_e_x",
    "f_o_r_c_e_d_s_e_x_forced sex",
    "forced sex",
    "forcedsex",
    "forcedsex_i n c e s t",
    "i n c e s t",
    "i-n-c-e-s-t",
    "i-n-c-e-s-t_i.n.c.e.s.t",
    "i.n.c.e.s.t",
    "i_n_c_e_s_t",
    "i_n_c_e_s_t_incest",
    "incest",
    "j a b a r d a s t i",
    "j a b a r d a s t i_j-a-b-a-r-d-a-s-t-i",
    "j-a-b-a-r-d-a-s-t-i",
    "j.a.b.a.r.d.a.s.t.i",
    "j.a.b.a.r.d.a.s.t.i_j4b4rd4571",
    "j4b4rd4571",
    "j_a_b_a_r_d_a_s_t_i",
    "j_a_b_a_r_d_a_s_t_i_jabardasti",
    "jabardasti",
    "m o l e s t",
    "m o l e s t a t i o n",
    "m o l e s t_m o l e s t a t i o n",
    "m-o-l-e-s-t",
    "m-o-l-e-s-t-a-t-i-o-n",
    "m-o-l-e-s-t_m-o-l-e-s-t-a-t-i-o-n",
    "m.o.l.e.s.t",
    "m.o.l.e.s.t.a.t.i.o.n",
    "m.o.l.e.s.t_m.o.l.e.s.t.a.t.i.o.n",
    "m0l357",
    "m0l3574710n",
    "m0l357_m0l3574710n",
    "m_o_l_e_s_t",
    "m_o_l_e_s_t_a_t_i_o_n",
    "m_o_l_e_s_t_m_o_l_e_s_t_a_t_i_o_n",
    "molest",
    "molest_molestation",
    "molestation",
    "non-consensual",
    "non-consensual_r a p e",
    "r a p e",
    "r a p e d",
    "r a p e d_r a p i n g",
    "r a p i n g",
    "r a p i s t",
    "r a p i s t_r-a-p-e",
    "r-a-p-e",
    "r-a-p-e-d",
    "r-a-p-e-d_r-a-p-i-n-g",
    "r-a-p-i-n-g",
    "r-a-p-i-s-t",
    "r-a-p-i-s-t_r.a.p.e",
    "r.a.p.e",
    "r.a.p.e.d",
    "r.a.p.e.d_r.a.p.i.n.g",
    "r.a.p.i.n.g",
    "r.a.p.i.s.t",
    "r.a.p.i.s.t_r4p157",
    "r4p157",
    "r4p1ng",
    "r4p1ng_r4p3",
    "r4p3",
    "r4p3d",
    "r4p3d_r_a_p_e",
    "r_a_p_e",
    "r_a_p_e_d",
    "r_a_p_e_d_r_a_p_i_n_g",
    "r_a_p_i_n_g",
    "r_a_p_i_s_t",
    "r_a_p_i_s_t_rape",
    "rape",
    "raped",
    "raped_raping",
    "raping",
    "rapist",
    "rapist_s e x t r a f f i c k i n g",
    "s e x t r a f f i c k i n g",
    "s e x u a l a b u s e",
    "s e x u a l a b u s e_s e x u a l a s s a u l t",
    "s e x u a l a s s a u l t",
    "s e x u e l l e r m i s s b r a u c h",
    "s e x u e l l e r m i s s b r a u c h_s t a t u t o r y r a p e",
    "s t a t u t o r y r a p e",
    "s t u p r o",
    "s t u p r o_s-e-x-t-r-a-f-f-i-c-k-i-n-g",
    "s-e-x-t-r-a-f-f-i-c-k-i-n-g",
    "s-e-x-u-a-l-a-b-u-s-e",
    "s-e-x-u-a-l-a-b-u-s-e_s-e-x-u-a-l-a-s-s-a-u-l-t",
    "s-e-x-u-a-l-a-s-s-a-u-l-t",
    "s-e-x-u-e-l-l-e-r-m-i-s-s-b-r-a-u-c-h",
    "s-e-x-u-e-l-l-e-r-m-i-s-s-b-r-a-u-c-h_s-t-a-t-u-t-o-r-y-r-a-p-e",
    "s-t-a-t-u-t-o-r-y-r-a-p-e",
    "s-t-u-p-r-o",
    "s-t-u-p-r-o_s.e.x.t.r.a.f.f.i.c.k.i.n.g",
    "s.e.x.t.r.a.f.f.i.c.k.i.n.g",
    "s.e.x.u.a.l.a.b.u.s.e",
    "s.e.x.u.a.l.a.b.u.s.e_s.e.x.u.a.l.a.s.s.a.u.l.t",
    "s.e.x.u.a.l.a.s.s.a.u.l.t",
    "s.e.x.u.e.l.l.e.r.m.i.s.s.b.r.a.u.c.h",
    "s.e.x.u.e.l.l.e.r.m.i.s.s.b.r.a.u.c.h_s.t.a.t.u.t.o.r.y.r.a.p.e",
    "s.t.a.t.u.t.o.r.y.r.a.p.e",
    "s.t.u.p.r.o",
    "s.t.u.p.r.o_s_e_x_t_r_a_f_f_i_c_k_i_n_g",
    "s_e_x_t_r_a_f_f_i_c_k_i_n_g",
    "s_e_x_u_a_l_a_b_u_s_e",
    "s_e_x_u_a_l_a_b_u_s_e_s_e_x_u_a_l_a_s_s_a_u_l_t",
    "s_e_x_u_a_l_a_s_s_a_u_l_t",
    "s_e_x_u_e_l_l_e_r_m_i_s_s_b_r_a_u_c_h",
    "s_e_x_u_e_l_l_e_r_m_i_s_s_b_r_a_u_c_h_s_t_a_t_u_t_o_r_y_r_a_p_e",
    "s_t_a_t_u_t_o_r_y_r_a_p_e",
    "s_t_u_p_r_o",
    "s_t_u_p_r_o_sex trafficking",
    "sex trafficking",
    "sextrafficking",
    "sextrafficking_sexual abuse",
    "sexual abuse",
    "sexual assault",
    "sexual assault_sexualabuse",
    "sexualabuse",
    "sexualassault",
    "sexualassault_sexueller missbrauch",
    "sexueller missbrauch",
    "sexuellermissbrauch",
    "sexuellermissbrauch_statutory rape",
    "statutory rape",
    "statutoryrape",
    "statutoryrape_stupro",
    "stupro",
    "tecavüz",
    "tecavüz_v e r g e w a l t i g u n g",
    "v e r g e w a l t i g u n g",
    "v i o l",
    "v i o l e n z a s e s s u a l e",
    "v i o l_v i o l e n z a s e s s u a l e",
    "v-e-r-g-e-w-a-l-t-i-g-u-n-g",
    "v-e-r-g-e-w-a-l-t-i-g-u-n-g_v-i-o-l",
    "v-i-o-l",
    "v-i-o-l-e-n-z-a-s-e-s-s-u-a-l-e",
    "v-i-o-l-e-n-z-a-s-e-s-s-u-a-l-e_v.e.r.g.e.w.a.l.t.i.g.u.n.g",
    "v.e.r.g.e.w.a.l.t.i.g.u.n.g",
    "v.i.o.l",
    "v.i.o.l.e.n.z.a.s.e.s.s.u.a.l.e",
    "v.i.o.l_v.i.o.l.e.n.z.a.s.e.s.s.u.a.l.e",
    "v10l",
    "v10l3nz4 5355u4l3",
    "v10l_v10l3nz4 5355u4l3",
    "v3rg3w4l71gung",
    "v3rg3w4l71gung_v_e_r_g_e_w_a_l_t_i_g_u_n_g",
    "v_e_r_g_e_w_a_l_t_i_g_u_n_g",
    "v_i_o_l",
    "v_i_o_l_e_n_z_a_s_e_s_s_u_a_l_e",
    "v_i_o_l_v_i_o_l_e_n_z_a_s_e_s_s_u_a_l_e",
    "vergewaltigung",
    "vergewaltigung_viol",
    "viol",
    "violación",
    "violación_violenza sessuale",
    "violenza sessuale",
    "violenzasessuale",
    "violenzasessuale_w i t h o u t c o n s e n t",
    "w i t h o u t c o n s e n t",
    "w-i-t-h-o-u-t-c-o-n-s-e-n-t",
    "w-i-t-h-o-u-t-c-o-n-s-e-n-t_w.i.t.h.o.u.t.c.o.n.s.e.n.t",
    "w.i.t.h.o.u.t.c.o.n.s.e.n.t",
    "w17h0u7 c0n53n7",
    "w17h0u7 c0n53n7_w_i_t_h_o_u_t_c_o_n_s_e_n_t",
    "w_i_t_h_o_u_t_c_o_n_s_e_n_t",
    "without consent",
    "without consent_withoutconsent",
    "withoutconsent",
    "z a b a r d a s t i",
    "z a b a r d a s t i_z-a-b-a-r-d-a-s-t-i",
    "z-a-b-a-r-d-a-s-t-i",
    "z.a.b.a.r.d.a.s.t.i",
    "z.a.b.a.r.d.a.s.t.i_z4b4rd4571",
    "z4b4rd4571",
    "z_a_b_a_r_d_a_s_t_i",
    "z_a_b_a_r_d_a_s_t_i_zabardasti",
    "zabardasti",
    "изнасилование",
    "изнасилование_сексуальное насилие",
    "сексуальное насилие",
    "جنسی تشدد",
    "جنسی تشدد_جنسی زیادتی",
    "جنسی زیادتی",
    "زبردستی ہمبستری",
    "زبردستی ہمبستری_زیادتی",
    "زیادتی",
    "छेड़छाड़",
    "छेड़छाड़_जबरन संभोग",
    "जबरन संभोग",
    "दुष्कर्म",
    "दुष्कर्म_पोक्सो",
    "पोक्सो",
    "बलात्कार",
    "बलात्कार_बाल यौन शोषण",
    "बाल यौन शोषण",
    "यौन उत्पीड़न",
    "यौन उत्पीड़न_यौन शोषण",
    "यौन शोषण",
    "forced intercourse",
    "sexual force",
    "sexual coercive act",
    "rape threat",
    "threatened rape",
    "sexual domination by force",
    "non voluntary sex",
    "sex against will",
    "sex under threat",
    "sex by intimidation",
    "sex by coercion",
    "forced intimacy",
    "forced penetration",
    "sexual violation act",
    "sexual violence act",
    "sexual crime",
    "sexual offence",
    "sexual felony",
    "sexual brutality",
    "sexual attack",
    "sexual battery",
    "sexual violation crime",
    "sexual exploitation crime",
    "sexual domination crime",
    "sexual misconduct",
    "sexual wrongdoing",
    "sexual harm",
    "sexual violation report",
    "rape case",
    "rape allegation",
    "rape accusation",
    "rape incident",
    "rape survivor",
    "rape victim",
    "rape trauma",
    "rape violence",
    "rape assault",
    "rape crime",
    "rape by force",
    "rape without consent",
    "rape of minor",
    "rape of child",
    "rape threat message",
    "rape intimidation",
    "rape coercion",
    "rape exploitation",
    "rape abuse",
    "rape wrongdoing",
    "rape violation",
    "rape offence",
    # English obfuscations / spacing
    "r a pe",
    "r a p e",
    "r-a-p-e",
    "r.a.p.e",
    "ra pe",
    "rap e",
    "ra-ped",
    "r@ ped",
    "r4 ped",
    "rap1st",
    "r a p i s t",
    "m o l e s t",
    "mol est",
    "mo lest",
    "m0 l e s t",
    "g r o p e",
    "gr op e",
    "gr0 p e",
    "grop ing",
    "f o r c e d s e x",
    "forced s e x",
    "f0rced sex",
    # Hinglish phrases
    "bina consent sex",
    "bina marzi sex",
    "jabardasti sambandh",
    "jabardasti physical",
    "jabardasti relation",
    "jabardasti samband",
    "jabardasti sharirik",
    "jabardasti hamla",
    "jabardasti yaun",
    "sex ke liye dhamki",
    "sex ke liye dabav",
    "sex ke liye pressure",
    "sex ke liye majboori",
    "sex ke liye zabardasti",
    "ladki ke sath zabardasti",
    "aurat ke sath zabardasti",
    "minor ke sath sex",
    "bacchi ke sath gandi harkat",
    "bacche ke sath sexual",
    "nabalig ke sath sex",
    # Hindi (Devanagari) expansions
    "जबरन यौन संबंध",
    "जबरन शारीरिक संबंध",
    "अनिच्छुक संभोग",
    "इच्छा के विरुद्ध संभोग",
    "बलपूर्वक संभोग",
    "बल से यौन संबंध",
    "यौन हमला",
    "यौन अपराध",
    "यौन हिंसक कृत्य",
    "यौन उत्पीड़न मामला",
    "यौन शोषण मामला",
    "नाबालिग से दुष्कर्म",
    "बालिका से दुष्कर्म",
    "महिला के साथ दुष्कर्म",
    "लड़की के साथ दुष्कर्म",
    "यौन अत्याचार",
    "लैंगिक अत्याचार",
    "जबरन छेड़छाड़",
    "अवैध यौन कृत्य",
    # Urdu (Arabic script) expansions
    "زبردستی جنسی تعلق",
    "زبردستی جنسی عمل",
    "رضامندی کے بغیر جنسی تعلق",
    "جنسی حملہ",
    "جنسی جرم",
    "جنسی زیادتی کا کیس",
    "بچوں کے ساتھ جنسی زیادتی",
    "لڑکی کے ساتھ زیادتی",
    "عورت کے ساتھ زیادتی",
    "نابالغ کے ساتھ جنسی عمل",
    # Spanish expansions
    "violacion forzada",
    "sexo sin consentimiento",
    "acto sexual forzado",
    "ataque sexual",
    "crimen sexual",
    "abuso sexual infantil",
    "violencia sexual",
    "coaccion sexual",
    "amenaza de violacion",
    # French expansions
    "viol sexuel",
    "rapport sexuel force",
    "rapport sans consentement",
    "crime sexuel",
    "violence sexuelle",
    "abus sexuel sur mineur",
    "agression sexuelle forcee",
    # Portuguese expansions
    "sexo forçado",
    "ato sexual forçado",
    "crime sexual",
    "violência sexual grave",
    "abuso sexual infantil",
    "coação sexual",
    # German expansions
    "erzwungener geschlechtsverkehr",
    "sex ohne einwilligung",
    "sexuelle gewalt",
    "sexuelles verbrechen",
    "missbrauch von kindern",
    "sexuelle noetigung",
    # Italian expansions
    "atto sessuale forzato",
    "sesso senza consenso",
    "reato sessuale",
    "violenza sessuale grave",
    "abuso sessuale su minori",
    # Russian expansions
    "принудительный секс",
    "секс без согласия",
    "сексуальное преступление",
    "сексуальное нападение",
    "насилие над детьми",
    "изнасилование угрозами",
    # Turkish expansions
    "zorla cinsel ilişki",
    "rıza olmadan seks",
    "cinsel suç",
    "cinsel saldırı suçu",
    "çocuğa cinsel istismar",
    # Indian language expansions
    "ಲೈಂಗಿಕ ಅಪರಾಧ",
    "ಲೈಂಗಿಕ ದೌರ್ಜನ್ಯ",
    "బలవంతపు లైంగిక సంబంధం",
    "లైంగిక నేరం",
    "ബലാത്സംഗ കേസ്",
    "ലൈംഗിക കുറ്റകൃത്യം",
    "ধর্ষণের ঘটনা",
    "যৌন অপরাধ",
    # Generic safety / threat phrasing
    "sex by threat",
    "sex by blackmail",
    "sex under duress",
    "sexual extortion",
    "sexual blackmail",
    "sexual threat",
    "sexual intimidation",
    "sexual pressure",
    "sexual force threat",
]


def parse_args():
    """
    Parse command-line arguments.
    """
    parser = argparse.ArgumentParser(description="Manipuraka Rape Repair")
    parser.add_argument("-i", "--input", type=str, help="Input text file to process.")
    parser.add_argument("-o", "--output", type=str, help="Output text file to write.")
    return parser.parse_args()


def read_file(file_path: str) -> str:
    """
    Read a text file and return the contents.
    """
    with open(file_path, "r") as file:
        return file.read()


def write_file(file_path: str, text: str) -> None:
    """
    Write text to a file.
    """
    with open(file_path, "w") as file:
        file.write(text)


def manipuraka_repair(text: str) -> str:
    """
    Redact/neutralize sexual-violence terms (multilingual) in a UTF-8-safe way.

    This function is intended for content moderation pipelines where you want to
    mask high-risk terms while keeping surrounding text intact.

    Args:
        text: Input text (UTF-8 Python str).

    Returns:
        Sanitized text with matched terms replaced by "[REDACTED_SV]".
    """
    if not text:
        return ""

    def _repl(match: re.Match[str]) -> str:
        # match.group(1) is the left "boundary" (maybe start or punctuation/space).
        # match.group(2) is the offending keyword/phrase.
        prefix = match.group(1) or ""
        return f"{prefix}[REDACTED_SV]"

    return MANIPURAKA_RAPE_PATTERN.sub(_repl, text)


def main():
    print(
        "Manipuraka Rape Repair: A simple Python script to redact/neutralize sexual-violence terms in a UTF-8-safe way.\n"
    )
    args = parse_args()
    if not args.input:
        print("Error: Input file is required.")
        return
    if not args.output:
        print("Error: Output file is required.")
        return
    input_text = read_file(args.input)
    output_text = manipuraka_repair(input_text)
    write_file(args.output, output_text)
    print(f"Processed {args.input} and wrote to {args.output}\n")


if __name__ == "__main__":
    main()
