import pytest

from Chess_Algorithm import Algorithm, df_raw, db, df_singlegame

# Check that the data includes the expected column names
def test_columns():
        df_raw.columns == {'Chess_ID', 'Game_id', 'Player_id', 'Move_id', 'Piece_id', 'Round_id', 'Time_id'},
        df_singlegame.columns =={'Player_id', 'Move_id', 'Round_id'}

# Check if there is data inside
def test_length_of_df():
    assert len(df_raw) != 0

def test_Algorithm():
    # check if it gives 4 outputs
    assert len(Algorithm("m4-l4")) == 4
    for i in range(len(Algorithm("m4-l4"))):
        # in each output check if there is a tuple of 2 elements, the first one is a string and the second a float
        assert len(Algorithm("m4-l4")[i]) == 2
        assert type(Algorithm("m4-l4")[i][0]) == str
        assert type(Algorithm("m4-l4")[i][1]) == float
    assert not Algorithm("idjid")






