// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;
pragma experimental ABIEncoderV2;

// struct CourseOfActionIDToPattern{ string coa_val; } string key = _ind_id - value = the structure. mapping id to pattern - can retrieve data using the id 
// mapping (string => CourseOfActionIDToPattern) contentIDs;
contract CourseOfActionStorage {
    
    string[] public course_of_actionIDs;
    string[] public contentIDs;

    struct CourseOfActionID{
        string stixID;
        string coa_val;
    }
    struct DataLocation{
        string contentID;
        string stixID;    
    }
    
    //QUERY THE DATA   string key = course_of_action, ID (ipv4,file hash, url etc) value = CourseOfAction for that pattern.  
    mapping (string => CourseOfActionID) course_of_action_list;
     
    //TIE THE ID TO THE CONTENT address ind_id - value = contentID. 
    mapping(string=> DataLocation) data_locations;
    
    
    function setCourseOfAction(string memory _contentID, string memory _stixID, string memory _coa_val) public {
        CourseOfActionID storage course_of_action = course_of_action_list[_coa_val];
        course_of_action.stixID= _stixID;
        course_of_action.coa_val = _coa_val;
        course_of_actionIDs.push(_stixID);
            
        DataLocation storage content = data_locations[_stixID];       
        content.contentID= _contentID;
        content.stixID = _stixID;
        contentIDs.push(_contentID);
    }
      
  function getContentIDs() view public returns(string[] memory){
      return contentIDs;
  }         
  
  function getCourseOfActions() view public returns(string[] memory){
      return course_of_actionIDs;
  }
  
  function getContentID(string memory _stixID) view public returns(string memory){
      return data_locations[_stixID].contentID;
  }         
  
  function getCourseOfAction(string memory _coa_val) view public returns (string memory){
      return course_of_action_list[_coa_val].stixID;

  }



}