// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;
pragma experimental ABIEncoderV2;

// struct ToolIDToPattern{ string ind_pat_val; } string key = _ind_id - value = the structure. mapping id to pattern - can retrieve data using the id 
// mapping (string => ToolIDToPattern) contentIDs;
contract ToolStorage {
    
    string[] public toolIDs;
    string[] public contentIDs;

    struct ToolID{
        string stixID;
        string tool_val;
    }
    struct DataLocation{
        string contentID;
        string stixID;    
    }
    
    //QUERY THE DATA   string key = tool, ID (ipv4,file hash, url etc) value = Tool for that pattern.  
    mapping (string => ToolID) tool_list;
     
    //TIE THE ID TO THE CONTENT address ind_id - value = contentID. 
    mapping(string=> DataLocation) data_locations;
    
    
    function setTool(string memory _contentID, string memory _stixID, string memory _tool_val) public {
        ToolID storage tool = tool_list[_tool_val];
        tool.stixID= _stixID;
        tool.tool_val = _tool_val;
        toolIDs.push(_stixID);
            
        DataLocation storage content = data_locations[_stixID];       
        content.contentID= _contentID;
        content.stixID = _stixID;
        contentIDs.push(_contentID);
    }
      
  function getContentIDs() view public returns(string[] memory){
      return contentIDs;
  }         
  
  function getTools() view public returns(string[] memory){
      return toolIDs;
  }
  
  function getContentID(string memory _stixID) view public returns(string memory){
      return data_locations[_stixID].contentID;
  }         
  
  function getTool(string memory _tool_val) view public returns (string memory){
      return tool_list[_tool_val].stixID;

  }



}