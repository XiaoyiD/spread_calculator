import pandas as pd
import unittest

# constant for input filename
INPUT_FILE = "sample_input.csv"


# ====================
# Helper functions for manipulating input file


def read_csv(filename):
    """ Return a pd.Dataframe of the given file input.

    :param file filename: a csv file contains data of corporate bond and
    government bond.
    :return pandas.core.frame.Dataframe: the dataframe of input file with cols
    bond, type, term, yield
    """

    df = pd.DataFrame()
    try:
        df = pd.read_csv(filename)
    except Exception as e:
        print("============== Reading File Error ================")
        print("Error: {}".format(e))
    return df


def format_data(df):
    """ Return corporate bonds dataframe and government bonds dataframe with
    the value in 'term' and 'yield' value are in float format .

    :param pd.Dataframe df: input dataframe with cols bond,type,term,yield
    :return: pd.Dataframe: dataframe in which cols 'term' and 'yield' are float
    """

    corporate_df = df.loc[df.type == 'corporate']
    government_df = df.loc[df.type == 'government']

    corp_df = corporate_df.copy()
    gov_df = government_df.copy()

    # modify the col 'term' and 'yield' into numeric values only
    corp_df.term = corporate_df['term'].apply(lambda x:
                                              float(x[:x.find(' ')]))

    gov_df.term = government_df['term'].apply(lambda x:
                                              float(x[:x.find(' ')]))
    corp_df['yield'] = corporate_df['yield'].apply(lambda x:
                                                   float(x[:x.find('%')]))
    gov_df['yield'] = government_df['yield'].apply(lambda x:
                                                   float(x[:x.find('%')]))
    return corp_df, gov_df


# ====================
# Helper functions for Challenge1 (yield spread calculation)


def find_best_benchmark(corporate_term, corporate_yield, government_bonds):
    """Return the candidate government bond name, and its yield of spread.

    The candidate government bond is the bond that most closest with the
    given corporate bond's term.

    :param float corporate_term: one corporate_bond's term
    :param float corporate_yield: one corporate_bond's yield
    :param pd.Dataframe government_bonds: a Dataframe of collections of
    government bonds info, with cols bond,type,term,yield
    :return str, float: the best candidate government bond's name, and the
    yield of spread with given corporate bond's yield
    """

    gov_term = government_bonds['term']
    difference = (gov_term - corporate_term).abs()
    candidate_loc = difference.idxmin()
    # candidate_benchmark = difference[select_gb_loc]
    candidate_name = government_bonds.loc[candidate_loc].bond
    spread = corporate_yield - government_bonds.loc[candidate_loc]['yield']
    spread = '%.2f' % spread    # reformat spread into 2-decimal float
    return candidate_name, spread


# ====================
# Helper functions for Challenge2 (spread curve generator)


def closest_to_corp(corporate_term, government_bonds):
    """  Return the candidate government bonds curve head and tail
    coordinates value.

    The candidate government bond is the bond that most closest with the
    given corporate bond's term.
    
    :param float corporate_term: current corporate_bond's term
    :param df.Dataframe government_bonds: a Dataframe of collections of
    government bonds info, with cols bond,type,term,yield
    :return float, float, float, float: head_x, head_y, tail_x, tail_y
    """
    gov_term = government_bonds['term']
    difference = (gov_term - corporate_term)
    pos_copy = difference[difference >= 0]
    neg_copy = difference[difference < 0]
    upper_gb_loc = pos_copy.idxmin()
    lower_gb_loc = neg_copy.abs().idxmin()
    g1_term = government_bonds.loc[upper_gb_loc].term
    g1_yield = government_bonds.loc[upper_gb_loc]['yield']
    g2_term = government_bonds.loc[lower_gb_loc].term
    g2_yield = government_bonds.loc[lower_gb_loc]['yield']
    return g1_term, g1_yield, g2_term, g2_yield


def linear_interpolation(g1_term, g1_yield, g2_term, g2_yield, c1_term):
    
    c1_curve_yield = g2_yield +\
               (c1_term - g2_term) * (g1_yield - g2_yield) / (g1_term - g2_term)
    return c1_curve_yield


def challenge1(df):
    """ Print the candidate brenchmark bond and its spread for each bond
    in df.

    :param pd.Dataframe df: General Dataframe of input file with both
    corporate bonds and government bonds
    :return None:
    """

    corp_bonds, gov_bonds = format_data(df)
    print("bond,benchmark,spread_to_benchmark")
    for i in range(corp_bonds.shape[0]):
        
        # Get basic info for current corp_bond
        corp_bond = corp_bonds.loc[i].bond
        corp_term = corp_bonds.loc[i].term
        corp_yield = corp_bonds.loc[i]['yield']

        # Find the benchmark bond for the corporate bond and calculate spread
        bond, spread = find_best_benchmark(corp_term, corp_yield, gov_bonds)
        print("{},{},{}%".format(corp_bond, bond, spread))



def challenge2(df):
    """ Print the candidate brenchmark bond and its spread to curve
    for each bond

    :param pd.Dataframe df: General Dataframe of input file with both 
    corporate bonds and government bonds
    :return None:
    """
    
    corp_bonds, gov_bonds = format_data(df)
    print("bond,spread_to_curve") 
    for i in range(corp_bonds.shape[0]):
        # Get basic info for current corp_bond
        corp_bond = corp_bonds.loc[i].bond
        corp_term = corp_bonds.loc[i].term
        corp_yield = corp_bonds.loc[i]['yield']

        # Find the curve's head and tail coordinates which
        # closest to current corp_bond
        g1_term, g1_yield, g2_term, g2_yield =\
            closest_to_corp(corp_term, gov_bonds)

        # Use Linear interpolation to find the yield of current corp_bond
        # on the curve above
        c1_curve_yield =\
            linear_interpolation(g1_term, g1_yield, g2_term, g2_yield, corp_term)

        # Convert spread into 2-deci floats
        spread_to_curve = '%.2f' % (corp_yield - c1_curve_yield)
        print("{},{}%".format(corp_bond, spread_to_curve))



if __name__ == "__main__":
    INPUT_FILE = input("Please type the full name of input file, suffix include:")
    df = read_csv(INPUT_FILE)
    challenge1(df)
    challenge2(df)