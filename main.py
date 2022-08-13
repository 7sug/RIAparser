from parse import parsing
from inserting import inserting


main_info = parsing.main_info_taker()
desc = parsing.description_taker(main_info)
inserting.data_correcting(desc)


