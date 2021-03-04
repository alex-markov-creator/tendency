import sys
import os

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from database import *

# Test module
#--------------------------------------------------------
import pytest
import datatest as dt
print(sys.path)
# Tests
# -------------------------------------------------------
class TestVersion():
    @pytest.mark.version
    def test_pd_version(self):
        """
        Checking the pandas library version
        """
        assert pd.__version__ >= '1.1.1'

class TestType():
    def test_type_1(self):
        """
        Should return an object of type list
        """
        assert isinstance(lst_name, list)
    @pytest.mark.one_value
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
    @pytest.mark.one_value
    @pytest.mark.parametrize('value' , lst_adhaesio)
    def test_type_4(self, value):
        """
        Should return an object of type pandas.DataFrame
        """
        assert isinstance(value,pd.DataFrame)

#class TestNotNull():
    #def test_add_raises():
        #with pytest.raises(pandas.errors.EmptyDataError):
            #raise pandas.errors.EmptyDataError

    #@pytest.mark.parametrize('value' , lst_name)
    #def test_null(self,value):
        #for i in value.columns:
            #for i in value[i]:
                #assert not pd.isna(i)

