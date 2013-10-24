ENV['DRQUEUE_MASTER'] ||= '10.12.39.161'
ENV['DRQUEUE_TMP'] ||= '/usr/local/drqueue/tmp'
ENV['DRQUEUE_ETC'] ||= '/usr/local/drqueue/etc'
ENV['DRQUEUE_LOGS'] ||= '/usr/local/drqueue/logs'
ENV['LDAP_TREEBASE'] ||= "dc=etcaes.com"
ENV['LDAP_HOST'] ||= "10.12.39.161"
ENV['LDAP_PORT'] ||= "389"
ENV['LDAP_FILTER'] ||= "uid"
ENV['LDAP_ATTRS'] ||= "cn"
ENV['WEB_PROTO'] ||= "http"
ENV['USER_STATUS'] ||= "demo,student,advanced,admin,geek"
ENV['USER_QUOTA'] ||= "0.5,5,15,35,50"
ENV['USER_PRIO'] ||= "100,500,750,1000,500"
ENV['USER_ADMIN_PW'] ||= "password"
ENV['LOG_SHOW_USER'] ||= "account name"
ENV['LOG_SHOW_PW'] ||= "password"
ENV['DQOR_USER'] ||= "drqueueonrails"
ENV['DQOR_GROUP'] ||= "drqueueonrails"
# ENV['AVAIL_RENDERERS'] ||= "blender,blenderlux,cinema4d,luxrender,maya,mayamr,mentalray,vray"
ENV['AVAIL_RENDERERS'] ||= "mentalray"
ENV['DQOR_TUTORIALS'] ||= "true"
ENV['DQOR_SHOW_FRAME_IMG'] ||= "true"
ENV['DQOR_SLAVES_CACHE_TIME'] ||= "600"
# APP_VERSION = IO.popen("git show --abbrev-commit | head -n 1").readline.split(" ")[1]
APP_VERSION = ""
RAILS_GEM_VERSION = '2.3.5' unless defined? RAILS_GEM_VERSION
require File.join(File.dirname(__FILE__), 'boot')
Rails::Initializer.run do |config|
  config.action_controller.session = { :session_key => "_dqor_session", :secret => "gfcgfkhjt56gfcdesxdtrr54w3fdxfhgffge55454565" } 
end
require 'will_paginate'
