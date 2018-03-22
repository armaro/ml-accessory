def fix_concat_dummies(dummyName, data):
  var = pd.get_dummies(data[dummyName], drop_first=True)
  data = pd.concat([data,var], axis=1)
  data = data.drop(dummyName, axis=1)
  return data
