import sys
import os

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from database import *

# Тестовый модуль
#--------------------------------------------------------
import pytest
import numpy as np
#Тестирование объектов pandas.DataFrame
from datatest import register_accessors, accepted, Invalid, Extra
# Тесты
# -------------------------------------------------------
class TestVersion():
    @pytest.mark.version
    def test_pd_version(self):
        """
        Checking the pandas library version
        """
        assert pd.__version__ >= '1.1.1'

class TestType():
    """
    Проверка типа данных исходников.
    list и pandas.DataFrame.
    """
    def test_type_1(self):
        """
        Should return an object of type list
        """
        assert isinstance(lst_name, list)
    @pytest.mark.data_test
    @pytest.mark.parametrize('value' , lst_name)
    def test_type_2(self, value):
        """
        Should return an object of type pandas.DataFrame
        """
        assert isinstance(value,pd.DataFrame)

    def test_type_3(self):
        """
        Should return an object of type list
        """
        assert isinstance(lst_adhaesio, list)
    @pytest.mark.data_test
    @pytest.mark.parametrize('value' , lst_adhaesio)
    def test_type_4(self, value):
        """
        Should return an object of type pandas.DataFrame
        """
        assert isinstance(value,pd.DataFrame)

class TestValidation():
    @pytest.mark.data_test
    @pytest.mark.parametrize('value' , lst_name)
    def test_validation_index_name(self, value):
        """
        Проверка на строковый тип данных имени индекса.
        Например, 'Год', 'Полугодие'
        Возможно регулярное значение в последующих версиях.
        """
        register_accessors()
        assert isinstance(value.index.name,str)

    @pytest.mark.data_test
    @pytest.mark.parametrize('value' , lst_name)
    def test_validation_index(self, value):
        """
        Проверка на целочисленное значение индекса.
        Например, 2008, 2018.
        """
        register_accessors()
        msg = 'Не целочисленное значение индекса'
        assert not value.index.validate(int)

    @pytest.mark.data_test
    @pytest.mark.parametrize('value' , lst_name)
    def test_validation_columns(self, value):
        """
        Проверка на строковый тип данных columns.
        Например, 'Уровень показателя в %'
        Возможно регулярное значение в последующих версиях.
        """
        register_accessors()
        assert not value.columns.validate(str)

    @pytest.mark.data_test
    @pytest.mark.parametrize('value' , lst_adhaesio)
    def test_validation_index_adhaesio(self, value):
        register_accessors()
        assert not value.index.validate(int)

    @pytest.mark.data_test
    @pytest.mark.parametrize('value' , lst_adhaesio)
    def test_validation_columns_adhaesio(self, value):
        register_accessors()
        assert not value.columns.validate(str)



"""
#class TestNotNull():
    #def test_add_raises():
        #with pytest.raises(pandas.errors.EmptyDataError):
            #raise pandas.errors.EmptyDataError

    #@pytest.mark.parametrize('value' , lst_name)
    #def test_null(self,value):
        #for i in value.columns:
            #for i in value[i]:
                #assert not pd.isna(i)

@pytest.mark.value_test
    @pytest.mark.parametrize('value' , lst_name)
    def test_validation_value(self, value):
        register_accessors()
        msg = 'Не вещественное или целочисленное значение показателя'
        assert not value.dropna().validate(float, msg=msg)

"""