import hashlib

def generate_finding_arn(product_name: str, resource_arn: str, security_control_id: str) -> str:

  def hash_key(string: str) -> str:
    hash_object = hashlib.md5()
    hash_object.update(string.encode())
    hex_digits = hash_object.hexdigest()

    # only keep half of the hash, to make it easier to use but still very unlikely for collisions.
    hex_digits = hex_digits[0:16]

    return hex_digits

  hash_this = product_name + resource_arn + security_control_id
  hashed = hash_key(hash_this)

  resource_arn_split = resource_arn.split(':') 
  partition = resource_arn_split[1]
  account = resource_arn_split[4]
  region = resource_arn_split[3]
  product_name = product_name.replace(' ','_')
  
  finding_arn = f"arn:{partition}:{product_name}:{region}:{account}/security-control/{security_control_id}/finding/{hashed}"

  return finding_arn
