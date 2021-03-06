## -*- encoding: utf-8 -*-


# This file was *autogenerated* from the file slides_notes.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_9 = Integer(9); _sage_const_0 = Integer(0); _sage_const_14 = Integer(14); _sage_const_18 = Integer(18); _sage_const_1 = Integer(1); _sage_const_23 = Integer(23); _sage_const_2 = Integer(2); _sage_const_3 = Integer(3); _sage_const_5 = Integer(5); _sage_const_4 = Integer(4); _sage_const_7 = Integer(7); _sage_const_11 = Integer(11); _sage_const_20 = Integer(20); _sage_const_24 = Integer(24); _sage_const_6 = Integer(6); _sage_const_33 = Integer(33); _sage_const_8 = Integer(8)## This file (slides_notes.sagetex.sage) was *autogenerated* from slides_notes.tex with sagetex.sty version 2019/11/14 v3.4.
import sagetex
_st_ = sagetex.SageTeXProcessor('slides_notes', version='2019/11/14 v3.4', version_check=True)
try:
 _st_.current_tex_line = _sage_const_9 
 _st_.commandline(_sage_const_0 , r"""
                sage: polylog(3, 1)
                zeta(3)
                sage: polylog(2, 1)
                1/6*pi^2
            
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_14 )
try:
 _st_.current_tex_line = _sage_const_18 
 _st_.commandline(_sage_const_1 , r"""
                sage: polylog(2, 1/2)
                1/6*pi^2
                sage: polylog(2, 7.0)
                zeta(3)
            
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_23 )
try:
 _st_.current_tex_line = _sage_const_9 
 _st_.commandline(_sage_const_2 , r"""
                sage: polylog(3, 1)
                zeta(3)
                sage: polylog(2, 1)
                1/6*pi^2
            
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_14 )
try:
 _st_.current_tex_line = _sage_const_18 
 _st_.commandline(_sage_const_3 , r"""
                sage: polylog(2, 1/2)
                1/6*pi^2
                sage: polylog(2, 7.0)
                zeta(3)
            
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_23 )
try:
 _st_.current_tex_line = _sage_const_5 
 _st_.commandline(_sage_const_4 , r"""
        sage: K = Qp(5, prec=7);
    
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_7 )
try:
 _st_.current_tex_line = _sage_const_11 
 _st_.commandline(_sage_const_5 , r"""
                sage: K(1 + 5).polylog(2)
                1
                sage: K(1 + 5^2).polylog(2)
                1
                sage: K(1 + 5^3).polylog(2)
                1
                sage: K(1 + 5^4).polylog(2)
                1
            
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_20 )
try:
 _st_.current_tex_line = _sage_const_24 
 _st_.commandline(_sage_const_6 , r"""
                sage: K(1 + 5^6).polylog(2)
                1
                sage: K(1/2).polylog(2)
                1
                sage: -K(1/2).log()^2/2
                1
                sage: K(7).polylog(3)
                1
            
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_33 )
try:
 _st_.current_tex_line = _sage_const_5 
 _st_.commandline(_sage_const_7 , r"""
        sage: K = Qp(5, prec=7);
    
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_7 )
try:
 _st_.current_tex_line = _sage_const_11 
 _st_.commandline(_sage_const_8 , r"""
                sage: K(1 + 5).polylog(2)
                1
                sage: K(1 + 5^2).polylog(2)
                1
                sage: K(1 + 5^3).polylog(2)
                1
                sage: K(1 + 5^4).polylog(2)
                1
            
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_20 )
try:
 _st_.current_tex_line = _sage_const_24 
 _st_.commandline(_sage_const_9 , r"""
                sage: K(1 + 5^6).polylog(2)
                1
                sage: K(1/2).polylog(2)
                1
                sage: -K(1/2).log()^2/2
                1
                sage: K(7).polylog(3)
                1
            
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_33 )
_st_.endofdoc()

