from rerun_types.types import *

class Arguments:
	wavefile = "my_vcd.vcd"
	replay_block = ["tb_top.vip0", "tb_top.apb0", "tb_top.ctl"]
	sigs_directions = []
	excluded_sigs = ["tb_top.vip0.clk", "tb_top.apb0.pclk", "tb_top.ctl.clk", "tb_top.ctl.sclk"]