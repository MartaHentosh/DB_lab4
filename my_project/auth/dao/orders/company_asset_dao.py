from typing import List

import sqlalchemy

from my_project.auth.dao.general_dao import GeneralDAO

from my_project.auth.domain.orders.company_asset import CompanyAsset
from sqlalchemy import text


class CompanyAssetDAO(GeneralDAO):
    """
    Realisation of Client data access layer.
    """
    _domain_type = CompanyAsset

    def procedure_insert_into_company_asset(self, assetName, assetType, employeeId, Cost):
        try:
            result = self._session.execute(text("CALL insert_into_company_asset(:p1, :p2, :p3, :p4)"),
                                           {"p1": assetName, "p2": assetType, "p3": employeeId,
                                            "p4": Cost})
            self._session.commit()
            return result.mappings()
        except Exception as e:
            print(f"Error executing stored procedure: {e}")
            self._session.rollback()
        return None

    def make_operation(self, operation):
        try:
            result = self._session.execute(
                sqlalchemy.text("CALL itcompany.make_operation_products(:p1)"),
                {"p1": operation}
            )

            # Fetch the result from the result set
            result_set = result.fetchall()

            # Close the result set
            result.close()

            # Commit the transaction
            self._session.commit()

            # Return the extracted data
            return result_set[0][0] if result_set else None

        except Exception as e:
            print(f"Error executing stored procedure: {e}")
            self._session.rollback()
            return None

    def insert_data(self):
        try:
            result = self._session.execute(sqlalchemy.text("CALL itcompany.insert_products()"))
            self._session.commit()
            return result.mappings()
        except Exception as e:
            print(f"Error executing stored procedure: {e}")
            self._session.rollback()
            return None

    def create_tables_for_cursor(self):
        result = self._session.execute(sqlalchemy.text("CALL itcompany.create_tables_for_cursor()"))
        self._session.commit()
        return result.mappings()
