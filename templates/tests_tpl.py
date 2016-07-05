# -*- coding: utf-8 -*-
import json

from ${package_name}.models import #foreach($t in $contract.typeRegistry().allTypes())
${t.name()}#if( $foreach.hasNext ),\\#end 
#end


#foreach($op in $contract.ops())
def test_${op.name()}_view(app):
    rv = app.get('/${op.name()}')
    data = json.loads(rv.data.decode('utf-8'))
    inst = ${op.responses().success().contractType().name()}()
    inst.from_dict(data)
    
  #foreach($f in $op.responses().success().contractType().fields())
  assert inst.${f.name()} is not None
  #end
#end


def test_swagger_info(app):
    rv = app.get('/api')
    spec = json.loads(rv.data.decode('utf-8'), 'utf-8')

    assert "info" in spec

    info = spec["info"]
    assert "title" in info
    assert info["title"] == "${package_name}"
    assert "version" in info
    assert info["version"] == "${version}"
    assert "description" in info
    assert info["description"] == "${description}"


#foreach($t in $contract.typeRegistry().allTypes())
def test_swagger_${t.name()}_definition(app):
    rv = app.get('/api')
    spec = json.loads(rv.data.decode('utf-8'), 'utf-8')

    definitions = spec["definitions"]
    assert "${t.name()}" in definitions

    definition = definitions["${t.name()}"]
    assert definition["type"] == "object"
    assert "properties" in definition

    props = definition["properties"]
#foreach($f in $t.fields())
    assert "${f.name()}" in props
    prop = props["${f.name()}"]
    
#set ($field_type = $f.contractType().name() )
#if( $field_type == "Integer")
    assert prop["format"] == "int32"
    assert prop["type"] == "integer"
#elseif( $field_type == "String")
    assert prop["type"] == "string"
#elseif( $field_type == "Boolean")
    assert prop["type"] == "boolean"
#elseif( $field_type == "Float")
    assert prop["format"] == "float"
    assert prop["type"] == "number"
#elseif( $field_type == "Date")
    assert prop["format"] == "date"
    assert prop["type"] == "string"
#elseif( $field_type == "DateTime")
    assert prop["format"] == "date-time"
    assert prop["type"] == "string"
#end

#end

#end
def test_swagger_parameters(app):
    rv = app.get('/api')
    spec = json.loads(rv.data.decode('utf-8'), 'utf-8')

    assert "parameters" in spec
    assert len(spec["parameters"]) == 0


#foreach($op in $contract.ops())
def test_swagger_${op.name()}_path(app):
    rv = app.get('/api')
    spec = json.loads(rv.data.decode('utf-8'), 'utf-8')

    assert "paths" in spec

    paths = spec["paths"]
    assert "/${op.path()}" in paths

    endpoint = paths["/${op.path()}"]
    assert "get" in endpoint

    get_op = endpoint["get"]
    assert "responses" in get_op

    responses = get_op["responses"]
    assert "${op.responses().success().code()}" in responses

    response_ok = responses["${op.responses().success().code()}"]
    assert "schema" in response_ok

    schema = response_ok["schema"]
    assert schema == {"$ref": "#/definitions/${op.responses().success().contractType().name()}"}
#end