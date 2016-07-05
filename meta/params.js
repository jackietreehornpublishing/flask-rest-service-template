function computed_parameters(m) {
  var now = new Date();
  return { creation_date: now.toISOString().split('T')[0] };
}
