from shutil import rmtree

from db_updater.importers.uls_data_retriever import UlsDataRetriever
from db_updater.utils import get_today_uls

SUNDAY = 6

if __name__ == '__main__':
    retriever: UlsDataRetriever
    if get_today_uls().weekday() == SUNDAY:
        retriever = UlsDataRetriever(complete=True,
                                     delete_all_current_entries=True,
                                     process_files_after_datetime=get_today_uls())
    else:
        retriever = UlsDataRetriever(complete=False)

    retriever.perform_import_from_uls()
    rmtree(retriever.data_importer.directory_path, ignore_errors=True)
