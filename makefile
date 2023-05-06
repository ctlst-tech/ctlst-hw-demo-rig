
atomics:
	@echo Generating atomics functions code
	@./catpilot/c-atom/tools/fspecgen.py --catom_path catpilot/c-atom --code --cmake --registry_c ./atomics_reg.c --atomics_dirs catpilot:catpilot/atomics/ctlst catom:catpilot/c-atom/atomics

xmlinline:
	@echo Inlining XML configs
	@./catpilot/c-atom/tools/xml2c_inliner.py --cfg_path config/ctlst/ --out xml_inline_cfgs.c

bblocks:
	@echo Generate description
	@./catpilot/c-atom/tools/fspecgen.py --catom_path catpilot/c-atom --code --cmake --bbxml bblocks.xml --atomics_dirs catpilot:catpilot/atomics/ catom:catpilot/c-atom/atomics/

ctlst:
	@echo Build
	rm -r -f build && cmake -DBOARD=ctlst -DCMAKE_BUILD_TYPE=Debug -B build && cd build && make catom-launcher

upload:
	@echo Upload config and firmware
	sh -c "./scripts/upload.sh ${ip}"
