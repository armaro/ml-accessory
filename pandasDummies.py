def fix_concat_dummies(dummyName):
  var = pd.get_dummies([dummyName], drop_first=True)
  data = pd.concat([data,var], axis=1)
  data = data.drop(dummyName, axis=1)
  return data
  
