
(cl:in-package :asdf)

(defsystem "water_executive-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "waterEvents" :depends-on ("_package_waterEvents"))
    (:file "_package_waterEvents" :depends-on ("_package"))
  ))