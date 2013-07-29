CKEDITOR.plugins.add('dropbox',
{
	requires : ['richcombo'],
	init: function( editor )
	{
		var config = editor.config;
		lang = editor.lang.format;
		var tags = [];
		tags[0] = ["[NOM]", "Nom", "Nom"];
		tags[1] = ["[PRENOM]", "Prenom", "Prenom"];
		tags[2] = ["[ENTREPRISE]", "Entreprise", "Entreprise"];
		editor.ui.addRichCombo('dropbox',
		{
			label : 'Tag',
			voiceLabel : "Insert tag",
			multiSelect : false,
			init:function(){
				for(var a in tags){
					this.add(tags[a][0],tags[a][1],tags[a][2]);
				}
			},
			
			panel :
            {
               css : [ config.contentsCss, CKEDITOR.getUrl( editor.skinPath + 'editor.css' ) ],
               voiceLabel : lang.panelVoiceLabel
            },
            
			onClick : function(value){
				for (name in CKEDITOR.instances){
					CKEDITOR.instances[name].insertHtml(value);
				}
				
				
			}
		});
	}
});