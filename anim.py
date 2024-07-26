from your_module import get_scraper

def check_scraper_exists(field_type_id):
    scraper = get_scraper(field_type_id)
    if scraper:
        return True
    else:
        return False
