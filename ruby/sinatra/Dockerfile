FROM ruby:2.5

WORKDIR /usr/src/app

COPY Gemfile Gemfile
COPY app.rb app.rb

RUN bundle install

ENV PORT 8090
EXPOSE 8090

CMD ["bundle", "exec", "ruby", "./app.rb"]
