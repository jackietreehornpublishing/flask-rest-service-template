function generate(po, mh) {
   var list = new ArrayList();
   var sc = po["contract"];
   var package = po["package_name"];
   if (sc) {
        list.add(new GeneratedFile(package + "/models.py", mh.merge(po, "models_tpl.py")));
        list.add(new GeneratedFile(package + "/views.py", mh.merge(po, "views_tpl.py")));
        list.add(new GeneratedFile(package + "/swagger.py", mh.merge(po, "swagger_tpl.py")));
        list.add(new GeneratedFile("tests/views_tests.py", mh.merge(po, "tests_tpl.py")));
   }
   return list;
}
