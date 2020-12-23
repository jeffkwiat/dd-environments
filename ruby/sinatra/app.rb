require 'sinatra'
require 'sinatra/reloader'
require 'ddtrace'

Datadog.configure do |c|
  c.tracer.enabled = true
  c.tracer.hostname = 'datadog-agent'
  c.tracer.port = 8126
  SERVICE_NAME = ENV['SERVICE_NAME'] || 'app-sinatra'

  c.diagnostics.debug = true

  c.use :sinatra, service: SERVICE_NAME
end

set :bind, '0.0.0.0'

get '/hello/:name' do
  "Hello #{params['name']}!"
end

get '/' do
  "Hello Ruby world!"
end
