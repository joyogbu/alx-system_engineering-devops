#!/usr/bin/env ruby
puts ARGV[0].scan(/(?<=from:).[a-z0-9]{1,}|(?<=to:).[a-z0-9]{1,}|(?<=flags:).[a-z\-:0-9]{1,}/).join(',')
