
import pandas as pd

def level2_json_df(data, data_start, level1_items, level2_tag):
    '''
    this function automatically creates a dataframe from an object nested within the 2nd level of a json dataset. 
    a list of 1st level column items to add is also specified, which will allow this df to be joined with others from the dataset
    '''
    tabledata = []
    for level1_item in data[data_start]:
        for level2_cntnr in level1_item[level2_tag]:
            record_dict = {}
            for level1_attr in level1_items:
                record_dict['record_'+level1_attr] = level1_item[level1_attr]       
            for level2_item in level2_cntnr.keys():
                record_dict[level2_tag+'_'+level2_item] = level2_cntnr[level2_item]
            tabledata.append(record_dict)
    return pd.DataFrame(tabledata)

