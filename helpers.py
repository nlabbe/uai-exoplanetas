### Funcion para agrupar las columnas con sus respectivos errores
def group_cols(mylist):
    groups = {}
    for i, col in enumerate(mylist):
        group = [x for x in mylist if col in x]
        if len(group) > 1 and col != 'ra':
            groups['group_' + str(i)] = group
    return groups

### Funcion para identificar columnas numéricas sabiendo las categoricas (incluso si se hacen dummies)
def identify_numeric(data, cat_cols=['koi_fpflag_nt', 'koi_fpflag_ss', 'koi_fpflag_co', 'koi_fpflag_ec', 'koi_tce_plnt_num']):
    cols = list(data.columns)
    ret_list = []
    for col in cols:
        add = True
        for y in cat_cols:
            add = add and (y not in col)
        if add:
            ret_list += [col]
    return ret_list
