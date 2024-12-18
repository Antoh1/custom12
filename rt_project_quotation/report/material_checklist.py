# -*- coding:utf-8 -*-

import base64
import io
from odoo import api, models


class MaterialChecklist(models.AbstractModel):
    _name = 'report.rt_project_quotation.report_material_checklist'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, quotations):
        sheet = workbook.add_worksheet("Material Checklist")
        user_company = self.env.user.company_id
        image = io.BytesIO(base64.b64decode(user_company.logo))
        bold = workbook.add_format({'bold': True, 'border': True, 'text_wrap': True})
        sheet.set_column("A:B", 30)
        sheet.set_column("C:D", 10)
        date_style = workbook.add_format({'bold': True, 'text_wrap': True, 'num_format': 'dd-mm-yyyy', 'border': True})
        long_text = workbook.add_format({'text_wrap': True, 'border': True})
        sheet.insert_image(1, 2, "logo.png", {'image_data': image, 'x_scale': 0.15, 'y_scale': 0.11})
        sheet.write(0, 0, 'CHECKLIST', bold)
        sheet.write(0, 1, 'FOR QUOTE: ' + quotations[0].name, bold)
        sheet.write(1, 0, 'CLIENT NAME', bold)
        sheet.write(1, 1, quotations[0].customer.name, bold)
        sheet.write(2, 0, 'PROJECT DETAILS', bold)
        sheet.write(2, 1, quotations[0].details, bold)
        sheet.write(3, 0, 'DATE', bold)
        sheet.write(3, 1, quotations[0].work_date, date_style)
        sheet.write(4, 0, 'PROJECT SECTION', bold)
        sheet.write(4, 1, 'ITEM(S)', bold)
        sheet.write(4, 2, 'QUANTITY', bold)
        sheet.write(4, 3, 'UNIT(S)', bold)

        row = 5
        for obj in quotations:
            if len(obj.planned_works) != 0 and obj.project_category:
                sheet.write(row, 0, 'Project :' + obj.project_category.name, bold)
                row += 1
                for work in obj.planned_works:
                    for material in work.materials_used:
                        section = ""
                        for item in material.items_used:
                            if section != work.name.name:
                                sheet.write(row, 0, work.name.name, long_text)
                            sheet.write(row, 1, item.item.name, long_text)
                            sheet.write(row, 2, item.item_qty, long_text)
                            sheet.write(row, 3, item.product_uom, long_text)
                            section = work.name.name
                            row += 1
            if len(obj.planned_works2) != 0 and obj.project_category2:
                sheet.write(row, 0, 'Project :' + obj.project_category2.name, bold)
                row += 1
                for work in obj.planned_works2:
                    for material in work.materials_used:
                        section = ""
                        for item in material.items_used:
                            if section != work.name.name:
                                sheet.write(row, 0, work.name.name, long_text)
                            sheet.write(row, 1, item.item.name, long_text)
                            sheet.write(row, 2, item.item_qty, long_text)
                            sheet.write(row, 3, item.product_uom, long_text)
                            section = work.name.name
                            row += 1
            if len(obj.planned_works3) != 0 and obj.project_category3:
                sheet.write(row, 0, 'Project :' + obj.project_category3.name, bold)
                row += 1
                for work in obj.planned_works3:
                    for material in work.materials_used:
                        section = ""
                        for item in material.items_used:
                            if section != work.name.name:
                                sheet.write(row, 0, work.name.name, long_text)
                            sheet.write(row, 1, item.item.name, long_text)
                            sheet.write(row, 2, item.item_qty, long_text)
                            sheet.write(row, 3, item.product_uom, long_text)
                            section = work.name.name
                            row += 1
            if len(obj.planned_works4) != 0 and obj.project_category4:
                sheet.write(row, 0, 'Project :' + obj.project_category4.name, bold)
                row += 1
                for work in obj.planned_works4:
                    for material in work.materials_used:
                        section = ""
                        for item in material.items_used:
                            if section != work.name.name:
                                sheet.write(row, 0, work.name.name, long_text)
                            sheet.write(row, 1, item.item.name, long_text)
                            sheet.write(row, 2, item.item_qty, long_text)
                            sheet.write(row, 3, item.product_uom, long_text)
                            section = work.name.name
                            row += 1
            if len(obj.planned_works5) != 0 and obj.project_category5:
                sheet.write(row, 0, 'Project :' + obj.project_category5.name, bold)
                row += 1
                for work in obj.planned_works5:
                    for material in work.materials_used:
                        section = ""
                        for item in material.items_used:
                            if section != work.name.name:
                                sheet.write(row, 0, work.name.name, long_text)
                            sheet.write(row, 1, item.item.name, long_text)
                            sheet.write(row, 2, item.item_qty, long_text)
                            sheet.write(row, 3, item.product_uom, long_text)
                            section = work.name.name
                            row += 1
            if len(obj.planned_works6) != 0 and obj.project_category6:
                sheet.write(row, 0, 'Project :' + obj.project_category6.name, bold)
                row += 1
                for work in obj.planned_works6:
                    for material in work.materials_used:
                        section = ""
                        for item in material.items_used:
                            if section != work.name.name:
                                sheet.write(row, 0, work.name.name, long_text)
                            sheet.write(row, 1, item.item.name, long_text)
                            sheet.write(row, 2, item.item_qty, long_text)
                            sheet.write(row, 3, item.product_uom, long_text)
                            section = work.name.name
                            row += 1
            if len(obj.planned_works7) != 0 and obj.project_category7:
                sheet.write(row, 0, 'Project :' + obj.project_category7.name, bold)
                row += 1
                for work in obj.planned_works7:
                    for material in work.materials_used:
                        section = ""
                        for item in material.items_used:
                            if section != work.name.name:
                                sheet.write(row, 0, work.name.name, long_text)
                            sheet.write(row, 1, item.item.name, long_text)
                            sheet.write(row, 2, item.item_qty, long_text)
                            sheet.write(row, 3, item.product_uom, long_text)
                            section = work.name.name
                            row += 1
