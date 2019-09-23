import os
import datetime
import remoclient
import spreadsheet

def update_column(sheet, line, values):
    cells = sheet.range(line, 1, line, len(values))
    for i in range(len(cells)):
        cells[i].value = values[i]
    sheet.update_cells(cells)

if __name__ == "__main__":
    gs = spreadsheet.SpreadSheet()
    sheet = gs.open_sheet(filename=os.environ['SHEET_NAME'])
    last_line = len(sheet.col_values(1))
    if last_line == 0:
        header = [
            'timestamp',
            'timestamp_unix',
            'temperature',
            'temperature_created_at',
            'humidity',
            'humidity_created_at',
            'illumination',
            'illumination_created_at',
            'motion',
            'motion_created_at'
        ]
        update_column(sheet, 1, header)
        last_line += 1

    now = datetime.datetime.now(datetime.timezone.utc)
    client = remoclient.NatureRemoClient()
    events = client.get_newest_events()
    now_iso = now.isoformat()

    values = [
        now_iso,
        int(now.timestamp()),
        events['te']['val'],
        events['te']['created_at'],
        events['hu']['val'],
        events['hu']['created_at'],
        events['il']['val'],
        events['il']['created_at'],
        events['mo']['val'],
        events['mo']['created_at']
    ]        
    update_column(sheet, last_line+1, values)
