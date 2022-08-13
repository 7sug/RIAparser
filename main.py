from parse import parse
from inserting import inserting


main_info = parse.main_info_taker()
desc = parse.description_taker(main_info)
inserting.data_correcting(desc)


