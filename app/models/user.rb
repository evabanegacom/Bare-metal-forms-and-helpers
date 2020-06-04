class User < ApplicationRecord
  validates :email, uniqueness: true, presence: true
  validates :username, uniqueness: true, presence: true, length: { minimum: 5 }
  validates :password, presence: true, length: { minimum: 6 }
  validates :password, confirmation: { case_sensitive: true }
end
