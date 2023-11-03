fun_content = '''
balanceOf(uint256,address)
onERC1155Received(address,address,uint256,uint256,bytes)
onERC1155BatchReceived(address,address,uint256[],uint256[],bytes)
balanceOf(address,uint256)
TransferSingle(address,address,address,uint256,uint256)
isApprovedForAll(address,address)
balanceOf(address,uint256)
safeTransferFrom(address,address,uint256,uint256,bytes)
safeBatchTransferFrom(address,address,uint256[],uint256[],bytes)
balanceOf(address,uint256)
balanceOfBatch(address[],uint256[])
setApprovalForAll(address,bool)
isApprovedForAll(address,address)
TransferSingle(address,address,address,uint256,uint256)
TransferBatch(address,address,address,uint256[],uint256[])  
ApprovalForAll(address,address,bool)
URI(string,uint256)
'''




fun_list = fun_content.split('\n')
