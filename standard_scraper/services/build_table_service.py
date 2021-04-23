from utils import clean_data_unit, clean_data_unit_no_spaces

class TableBuilderService:

    def __init__(self, logger):
        self.logger = logger

    def get_table(self, html, id, row_tag, col_tag, expected_headers):
        rows = []
        try:
            self.logger.info("Reading rows...")
            soup = BeautifulSoup(html, 'html.parser')
            table = soup.select_one(id)
            self.logger.info("Table found.")
            rows = table.findAll(lambda tag: tag.name == row_tag)
            self.logger.info("Rows read.")
        except:
            self.logger.error("ERROR: No data found, no rows to parse")
        headers, analytes = self.remove_markup(rows, col_tag, expected_headers)
        return headers, analytes

    def remove_markup(self, rows, col_tag, expected_headers):
        #Removes HTML from rows and headers
        headers = self.get_headers(col_tag, expected_headers)
        self.logger.info("Headers received.")
        analytes = self.get_analytes(rows)
        return headers, analytes

    def get_headers(self, col_tag, expected_headers):
        header_row = data_rows.pop(0)
        headers = header_row.find_all(col_tag)
        headers = self.clean_headers(headers, expected_headers)
        return headers
    
    def clean_headers(self, headers, expected_headers):
        # Provide header list
        parsed_headers = []
        for ele in headers:
            new_header = clean_data_unit_no_spaces(ele.text)
            for expected_header in expected_headers:
                if new_header in expected_header:
                    parsed_headers.append(expected_header)
                    break;
        self.logger.info(parsed_headers)
        return parsed_headers

    def get_analytes(self, rows, col_tag):
        self.logger.info("Cleaning data...")
        analytes = []
        for row in rows:
            cols = row.find_all(col_tag)
            clean_row = self.build_row(cols)
            analytes.append(clean_row)
        return analytes
    def build_row(self, cols):
        clean_row = []
        href = ''
        for i, ele in enumerate(cols):
            data = clean_data_unit(ele.text)
            if self.chem_scrape == 'CHEM':
                if ele.a is not None:
                    href = self.url + "JSP/" + ele.a['href']
                    href = href.replace(' ', '')
            if data or i < len(self.expected_headers) - 1:
                if data == '':
                    data = 'NULL'
                clean_row.append(data)
        if self.chem_scrape == 'CHEM':
            clean_row.append(href)
        return clean_row