# -*- coding: utf-8 -*-
from flask import jsonify

from ${package_name}.service import app
from ${package_name}.models import #foreach($t in $contract.typeRegistry().allTypes())
${t.name()}#if( $foreach.hasNext ),\\#end 
#end


__all__ = [#foreach($op in $contract.ops())'${op.name()}'#if( $foreach.hasNext ), #end#end]


#foreach($op in $contract.ops())
@app.route('/${op.path()}')
def ${op.name()}(#foreach($p in $op.parameters())$p.name()#if( $foreach.hasNext ), #end#end):
    v = ${op.responses().success().contractType().name()}()
    return jsonify(v.to_dict())
#end
