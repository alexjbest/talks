set table "slides.grank1.table"; set format "%.5f"
set format "%.7e";; set contour base; set cntrparam levels discrete 0.003; unset surface; set view map; set samples 700; set isosamples 500; splot y**2+ (x**3 + x + 1)*y +x**2 + x; 
